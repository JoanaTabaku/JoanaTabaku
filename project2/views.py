from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')

def contact(request):
    return render(request, 'product.html')