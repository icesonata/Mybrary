from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=16)
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    publish_date = models.CharField(max_length=32)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    ratings_count = models.IntegerField()
    page_count = models.IntegerField()
    description = models.CharField(max_length=4096)

    def __str__(self):
        return f"""
                isbn: {self.isbn}\n
                title: {self.title}\n
                author: {self.author}\n
                publisher: {self.publisher}\n
                publish_date: {self.publish_date}\n
                average rating: {self.average_rating}\n
                ratings count: {self.ratings_count}\n
                page count: {self.page_count}\n
                description: {self.description}
                """

