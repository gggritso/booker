from django.http import JsonResponse
from .models import Book


def index(request):
    books = Book.objects.all()[:10]
    return JsonResponse(
        {"books": [{"name": book.title, "author": book.author} for book in books]}
    )
