
from django.db.models import Count
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers  import ProductsSerializer
from product.utils import distribution
from product.models import Product, Author, Lesson

def v1(request):
    id_product = 1
    lessons = Lesson.objects.select_related('product').values('product_id').annotate(count_lesson=Count('id'))
    products = Product.objects.all()
    for i in lessons:
        pass
    return HttpResponse("get")

@api_view(['GET', 'POST'])
def list_product_api(request):
    pass