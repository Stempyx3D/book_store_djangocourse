

from django.contrib import admin
from .models import Adress, Author, Book, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'is_bestselling', 'price', 'publication_date')
    list_filter = ('is_bestselling', 'publication_date')
    search_fields = ('title', 'author__first_name', 'author__last_name')
    prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Country)
admin.site.register(Adress)



