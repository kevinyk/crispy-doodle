from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pizza

# Create your views here.
def index(request):
    context = {'all_pizzas': Pizza.objects.all()}
    return render(request, 'first_app/index.html', context )

def create(request):

    if request.method == "POST":
        # 1. Call the manager function
        pizza = Pizza.objects.validate_pizza(request.POST)
        
        # 5. Check if errors exist, if they do, add them to messages
        if 'errors' in pizza:
            for key,value in pizza['errors'].items():
                messages.error(request, value)
        else:
            messages.success(request, 'YOU DID IT')
        return redirect('/')
