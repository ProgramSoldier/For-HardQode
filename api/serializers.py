from rest_framework import serializers
from django.db import models
from product.models import Product, Author

class ProductsSerializer(serializers.Serializer):
    title = models.CharField(max_length=150)
    date_start = models.DateTimeField()
    price = models.IntegerField()
    max_size_group = models.IntegerField()
    min_size_group = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    lesson_count = models.IntegerField()
