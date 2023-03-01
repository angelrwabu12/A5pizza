from django.shortcuts import render, redirect,get_object_or_404
from .models import PizzaStock
from .forms import PizzaForm

# Create your views here.
def home(request):
    pizzas = PizzaStock.objects.all()
    return render(request, 'index.html', {'pizzas':pizzas})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def registration(request):
    if request.method =='POST':
        form =PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=PizzaForm()
    return render(request, 'registration.html', {'form':form})
def login(request):
    return render(request, 'login.html')
def pizzadetail(request,pk):
    pizza=get_object_or_404(PizzaStock,pk=pk)
    return render(request,'pizzadetail.html',{'pizza':pizza})

    