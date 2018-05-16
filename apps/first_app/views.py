from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pizza

# Create your views here.
def index(request):
    context = {'all_pizzas': Pizza.objects.all()}
    return render(request, 'first_app/index.html', context)

def create(request):
    if request.method == "POST":
        # Original validation logic applies
        # Name must be present and at least 2 characters long
        # Description must be present and at least 8 characters
        # price must be present
        print(request.POST)
        # 1. create errors dictionary
        errors = {}
        # 2. validate post information
        if len(request.POST['name']) == 0:
            errors['name'] = "Name must be present"
        elif len(request.POST['name'])<2:
            errors['name'] = "Name must be at least 2 characters long"

        if len(request.POST['price']) == 0:
            errors['price'] = "Price must be present"
        
        if len(request.POST['description']) == 0:
            errors['description'] = "Description is required"
        elif len(request.POST['description']) < 8:
            errors['description'] = "Description must be at least 8 characters long"
        print(errors)
        # 3. Check if errors exist, if they do, add them to messages
        if len(errors):
            for key,value in errors.items():
                messages.error(request, value)
        else:
            Pizza.objects.create(name = request.POST['name'], price = request.POST['price'], description = request.POST['description'])
        return redirect('/')