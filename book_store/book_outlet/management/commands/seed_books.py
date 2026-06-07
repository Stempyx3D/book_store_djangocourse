from datetime import date

from django.core.management.base import BaseCommand

from book_outlet.models import Author, Book


class Command(BaseCommand):
    help = "Create 10 test books in the database."

    def handle(self, *args, **options):
        books = [
            {
                "title": "Django in Action",
                "author": {"first_name": "Maya", "last_name": "Stone"},
                "rating": 5,
                "is_bestselling": True,
                "price": 29.99,
                "publication_date": date(2024, 1, 12),
            },
            {
                "title": "Python Patterns",
                "author": {"first_name": "Avery", "last_name": "Cole"},
                "rating": 4,
                "is_bestselling": False,
                "price": 24.50,
                "publication_date": date(2023, 8, 20),
            },
            {
                "title": "API Design Basics",
                "author": {"first_name": "Jordan", "last_name": "Lee"},
                "rating": 4,
                "is_bestselling": True,
                "price": 31.00,
                "publication_date": date(2022, 11, 5),
            },
            {
                "title": "Clean Code Notes",
                "author": {"first_name": "Sam", "last_name": "Patel"},
                "rating": 5,
                "is_bestselling": False,
                "price": 19.95,
                "publication_date": date(2021, 5, 14),
            },
            {
                "title": "Modern Databases",
                "author": {"first_name": "Elena", "last_name": "Ross"},
                "rating": 3,
                "is_bestselling": False,
                "price": 27.25,
                "publication_date": date(2023, 2, 9),
            },
            {
                "title": "Testing Django Apps",
                "author": {"first_name": "Noah", "last_name": "Kim"},
                "rating": 5,
                "is_bestselling": True,
                "price": 22.75,
                "publication_date": date(2024, 4, 2),
            },
            {
                "title": "Git for Teams",
                "author": {"first_name": "Olivia", "last_name": "Hart"},
                "rating": 4,
                "is_bestselling": False,
                "price": 16.99,
                "publication_date": date(2020, 9, 30),
            },
            {
                "title": "Frontend with Django",
                "author": {"first_name": "Liam", "last_name": "Fox"},
                "rating": 3,
                "is_bestselling": True,
                "price": 28.40,
                "publication_date": date(2022, 7, 18),
            },
            {
                "title": "Deployment Recipes",
                "author": {"first_name": "Chloe", "last_name": "Reed"},
                "rating": 4,
                "is_bestselling": False,
                "price": 34.10,
                "publication_date": date(2024, 6, 1),
            },
            {
                "title": "Scaling Small Apps",
                "author": {"first_name": "Ethan", "last_name": "Brooks"},
                "rating": 5,
                "is_bestselling": True,
                "price": 39.90,
                "publication_date": date(2023, 12, 25),
            },
        ]

        created_count = 0
        updated_count = 0
        author_created_count = 0

        for book_data in books:
            author_data = book_data["author"]
            author, author_created = Author.objects.get_or_create(
                first_name=author_data["first_name"],
                last_name=author_data["last_name"],
            )
            if author_created:
                author_created_count += 1

            book_defaults = {
                key: value for key, value in book_data.items() if key != "author"
            }
            book_defaults["author"] = author

            _, created = Book.objects.update_or_create(
                title=book_data["title"],
                defaults=book_defaults,
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded 10 books. Created: {created_count}, updated: {updated_count}. Authors created: {author_created_count}."
            )
        )