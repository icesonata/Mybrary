from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=16)      # isbn 13
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=128)
    publish_date = models.CharField(max_length=32)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    ratings_count = models.IntegerField()
    page_count = models.IntegerField()
    description = models.CharField(max_length=4096)

    def __str__(self):
        return f"""
                isbn: {self.isbn}
                title: {self.title}
                author: {self.author}
                publish_date: {self.publish_date}
                average rating: {self.average_rating}
                ratings count: {self.ratings_count}
                page count: {self.page_count}
                description: {self.description}
                """

class Profile(models.Model):
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='usr')
    # image = models.ImageField(default='default.jpg', upload_to='usr')
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)