import sys
import csv
import argparse
from django.core.management.base import BaseCommand
from books.models import Book, Author


class Command(BaseCommand):
    help = "Load book data from CSV"

    def add_arguments(self, parser):
        parser.add_argument("source", type=argparse.FileType("r"), default=sys.stdin)

    def handle(self, source):
        reader = csv.DictReader(source)

        for row in reader:
            try:
                author = Author.objects.get(id=int(row["id"]))
            except Author.DoesNotExist:
                author = Author(name=row["author"])
                author.save()

            try:
                book = Book.objects.get(id=int(row["id"]))
            except Book.DoesNotExist:
                book = Book(id=row["id"], title=row["title"], author=author)
                book.save()

            print(book)

        print("Done")
