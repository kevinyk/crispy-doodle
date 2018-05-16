from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pizza
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt

# Create your views here.
def index(request):
    context = {'all_pizzas': Pizza.objects.all()}
    return render(request, 'first_app/index.html', context)

def create(request):
    if request.method == "POST":
        
        result = Pizza.objects.validate_registration(request.POST)
        if 'errors' in result:
            for key,value in result['errors'].items():
                messages.error(request, value)
        else:
            messages.success(request, "Welcome to the club!")
        return redirect('/')


def login(request):
    if request.method == "POST":
        users_with_same_email = Pizza.objects.filter(email = request.POST['email'])
        if len(users_with_same_email) > 0:
            print('user with the email exists! checking passswords now....')
            the_user = users_with_same_email.first()
            if bcrypt.checkpw(request.POST['password'].encode(), the_user.password.encode()):
                print('the passwords match! adding to session')
                request.session['user_id'] = the_user.id
                request.session['user_name'] = the_user.name
                messages.success(request, 'you have logged in, {}!'.format(request.session['user_name']))
                return redirect('/')
            else:
                print('passwords do not match')
                messages.error(request, "invalid info")
                return redirect('/')
        else:
            messages.error(request, "invalid info, no users with that email")
            return redirect('/')