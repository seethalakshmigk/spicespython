from django.shortcuts import render
from shop.models import Product
from  django.db.models import Q

def search_result(request):
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).distinct()

    return render(request, 'search.html', {'query': query, 'products': products})
