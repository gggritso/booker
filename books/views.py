from django.http import JsonResponse
from .models import Book


def index(request):
    books = Book.objects.all()[:10]
    return JsonResponse(
        {
            "books": [
                {
                    "id": book.id,
                    "name": book.title,
                    "author": {"id": book.author.id, "name": book.author.name},
                }
                for book in books
            ]
        }
    )
