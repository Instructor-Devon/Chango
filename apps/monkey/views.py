from django.shortcuts import render, HttpResponse, redirect
from .models import Monkey
import re
import bcrypt
from django.contrib.messages import error

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# Create your views here.
# localhost:8000
def index(request):
    # return 'HELLO WORLD"

    # checking in monkeyId is in session, getting a monkey with that id
    # we could also just check if monkeyId is a key in session dict
    try:
        currMonkey = Monkey.objects.get(id=request.session['monkeyId'])
    except:
        currMonkey = None

    context = {
        "monkies": Monkey.objects.all(),
        "monkey": currMonkey
    }
    return render(request, 'monkey/index.html', context)

# localhost:8000/monkey
def monkey(request):
    return HttpResponse("MONKEY")

def registration(request):
    
    # let's see what we submitted!
    if request.method == 'POST':
        print(request.POST)

        errors = []
        if(len(request.POST['first_name']) < 1):
            errors.append("First Name is required!")
        
        if(len(request.POST['last_name']) < 1):
            errors.append("Last Name is required!")
        
        if(len(request.POST['email']) < 1):
            errors.append("Email is required!")
        
        if(len(request.POST['password']) < 1):
            errors.append("Password is required!")  

        if(request.POST['password'] != request.POST['confirm']):
            errors.append("Passwords no match")

        if not re.match(EMAIL_REGEX, request.POST['email']):
            errors.append("Invalid Email")

        # are there not any items in errors?
        if not errors:
            # hash the passs!!
            hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            newMonkey = Monkey.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], phone_number=request.POST["phone_number"], password=hashed)
            request.session['monkeyId'] = newMonkey.id

        else:
            # flash a message for each item in errors!
            for err in errors:
                error(request, err)


        print(errors)


        return redirect('/registration')
    print("bout to render a template from reg lol")
    return render(request, 'monkey/registration.html')

def show(request, monkey_id):
    # Get monkey by id
    monkey = Monkey.objects.get(id=monkey_id)

    context = {
        "monkey": monkey
    }

    return render(request, 'monkey/show.html', context)

def name(request, monkey_name):

    return HttpResponse(monkey_name)