from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def index(request):
    # Зчитування необхідних даних із БД
    page_size = 6
    all_products = Product.objects.all()

    paginator = Paginator(all_products, page_size)
    page_number = request.GET.get('page')
    paginate_products = paginator.get_page(page_number)
    return render(request, 'catalog/index.html', context={
        'title': 'Каталог товарів',
        'paginate_products': paginate_products,
        'all_categories': Category.objects.all(),
        'all_producers': Producer.objects.all()
    })
