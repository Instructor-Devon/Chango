from django.shortcuts import render, HttpResponse, redirect
from .models import Monkey, Post
import re
import bcrypt
from django.contrib.messages import error

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
MONKEY_KEY = 'monkeyId'

# Create your views here.
# localhost:8000
def index(request):

    return render(request, 'monkey/index.html')

# localhost:8000/monkey
def monkey(request):
    return HttpResponse("MONKEY")

def login(request):
    
    if request.method == 'POST':
        # validate login
        errors = []
        # check if email in db
        userCheck = Monkey.objects.filter(email=request.POST['email'])

        # is there a empty list?
        if not userCheck:
            errors.append("Invalid Email/Password")
        else:
            if not bcrypt.checkpw(request.POST['password'].encode(), userCheck[0].password.encode()):
                errors.append("Invalid Email/Password")

        if errors:
            for e in errors:
                error(request, e)
            return redirect('/')
        request.session[MONKEY_KEY] = userCheck[0].id
        return redirect('/dashboard')
        
    return redirect('/')

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
            request.session[MONKEY_KEY] = newMonkey.id

        else:
            # flash a message for each item in errors!
            for err in errors:
                error(request, err)

            print(errors)
            return redirect('/')



        return redirect('/dashboard')

def dashboard(request):

    try:
        monkey_id = request.session[MONKEY_KEY]
    except:
        return redirect('/')
    context = {
        "monkey": Monkey.objects.get(id=monkey_id),
        "posties": Post.objects.all()
    }
    return render(request, 'monkey/dashboard.html', context)

def show(request, monkey_id):
    # Get monkey by id
    monkey = Monkey.objects.get(id=monkey_id)

    context = {
        "monkey": monkey
    }

    return render(request, 'monkey/show.html', context)

def name(request, monkey_name):

    return HttpResponse(monkey_name)

def newPost(request):

    if request.method == "GET":
        return redirect("/dashboard")

    # no empty post content!
    errors = []
    if len(request.POST['content']) < 1:
        errors.append("Post must not be empty")
    # no posts longer than 255
    if len(request.POST["content"]) > 255:
        error.append("Let's not write a novel there buddy")
    
    if errors:
        for e in errors:
            error(request, e)
        return redirect('/dashboard')

    thisMonkey = Monkey.objects.get(id=request.session[MONKEY_KEY])
    Post.objects.create(content = request.POST['content'], author=thisMonkey)

    return redirect("/dashboard")