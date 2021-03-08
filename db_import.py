import csv
from django.db import models
from bookstore.models import Book

def add_book():
    with open("bookdb/books.csv") as f:
        reader = csv.reader(f)
        header = next(reader)       # skip the first line which is a field description
        for item in reader:
            dt = Book(
                isbn=item[11],
                title=item[1],
                author=item[2],
                publish_date=item[13],
                average_rating=item[3],
                ratings_count=item[4],
                page_count=item[9],
                description=item[7]      
            )
            dt.save()
            print(f"Added {dt.isbn}")

if __name__ == '__main__':
    add_book()