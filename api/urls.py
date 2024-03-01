from django.urls import path, include
from .views import v1
urlpatterns = [
    path('v1/', v1, name='v1'),

]