from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Group(models.Model):
    title = models.CharField(max_length=100)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Group_Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    visibility = models.BooleanField(default=True)
