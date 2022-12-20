from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)  
    
    return render(request,'index.html', {'product_object': product_object})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request,'detail.html', {'product': product_object})


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')