from django.contrib import admin
from .models import Student, Group, Group_Student

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Group_Student)
