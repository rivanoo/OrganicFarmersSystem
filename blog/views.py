from django.shortcuts import render, redirect
from .forms import FarmerForm, ProductForm
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def farmer_register(request):
    if request.method == "POST":
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FarmerForm()

    return render(request, 'farmer_register.html', {'form': form})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})
