from django.http import JsonResponse
from .models import Book, Author


def index(request):
    books = Book.objects.all()[:10]
    return JsonResponse(
        {
            "books": [
                {
                    "id": book.id,
                    "title": book.title,
                    "author": {"id": book.author.id, "name": book.author.name},
                }
                for book in books
            ]
        }
    )


def by_author(request):
    authors = Author.objects.filter(name__icontains=request.GET["name"])
    books = Book.objects.filter(author__in=authors)

    return JsonResponse(
        {
            "authors": [
                {
                    "id": author.id,
                    "name": author.name,
                }
                for author in authors
            ],
            "books": [
                {"id": book.id, "title": book.title, "author": {"id": book.author.id}}
                for book in books
            ],
        }
    )
