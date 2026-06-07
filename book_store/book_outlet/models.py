from pyexpat import model

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)


    def __str__(self):
        return f"{self.name} ({self.code})"
    
    class Meta:
        verbose_name_plural = "Countries"

class Adress(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.city}, {self.street} {self.postal_code}"
    
    class Meta:
        verbose_name_plural = "Adresses"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Adress, on_delete=models.CASCADE, null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publication_date = models.DateField()
    slug = models.SlugField(default='', null=False, blank=True, db_index=True)
    published_countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author} (Rating: {self.rating})"






