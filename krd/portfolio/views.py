from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product_page(request):
    return render(request, 'product_page.html')

# Create your views here.
