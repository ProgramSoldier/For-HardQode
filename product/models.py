from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=150)
    date_start = models.DateTimeField()
    price = models.IntegerField()
    max_size_group = models.IntegerField()
    min_size_group = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
