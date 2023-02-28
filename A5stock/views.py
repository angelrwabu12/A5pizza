from django.shortcuts import render
from .models import PizzaStock
# Create your views here.
def home(request):
    pizzas = PizzaStock.objects.all()
    return render(request, 'index.html', {'pizzas':pizzas})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
