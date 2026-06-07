from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg, Max, Min

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('-rating')
    books_counts = books.count()
    average_rating = books.aggregate(Avg('rating'))['rating__avg']
    max_rating = books.aggregate(Max('rating'))['rating__max']
    min_rating = books.aggregate(Min('rating'))['rating__min']
    bestsellers = Book.objects.filter(is_bestselling=True).order_by('-rating')
    return render(request, 'book_outlet/index.html', {'books': books,
                                                      'books_counts': books_counts,
                                                      'average_rating': average_rating,
                                                      'max_rating': max_rating,
                                                      'min_rating': min_rating,
                                                      'bestsellers': bestsellers})

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=book_id)
    # except Book.DoesNotExist:
    #     return render(request, '404.html', status=404)
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {'book': book})
