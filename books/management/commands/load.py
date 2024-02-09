import sys
import csv
import argparse
from django.core.management.base import BaseCommand
from books.models import Book, Author


class Command(BaseCommand):
    help = "Load book data from CSV"

    def add_arguments(self, parser):
        parser.add_argument("source", type=argparse.FileType("r"), default=sys.stdin)

        parser.add_argument("--book-id-field", default="id")
        parser.add_argument("--author-field", default="author")
        parser.add_argument("--title-field", default="title")

    def handle(self, *args, **options):
        reader = csv.DictReader(options["source"])

        for row in reader:
            try:
                author = Author.objects.get(name=row[options["author_field"]])
            except Author.DoesNotExist:
                author = Author(name=row[options["author_field"]])
                author.save()

            try:
                book = Book.objects.get(id=int(row[options["book_id_field"]]))
            except Book.DoesNotExist:
                book = Book(
                    id=row[options["book_id_field"]],
                    title=row[options["title_field"]],
                    author=author,
                )
                book.save()

            print(book)

        print("Done")
