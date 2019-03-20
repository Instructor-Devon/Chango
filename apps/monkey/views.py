from django.shortcuts import render, HttpResponse
from .models import Monkey
# Create your views here.
# localhost:8000
def index(request):
    # return 'HELLO WORLD"

    context = {
        "monkies": Monkey.objects.all()
    }
    return render(request, 'monkey/index.html', context)

# localhost:8000/monkey
def monkey(request):
    return HttpResponse("MONKEY")

def show(request, monkey_id):
    # Get monkey by id
    monkey = Monkey.objects.get(id=monkey_id)

    context = {
        "monkey": monkey
    }

    return render(request, 'monkey/show.html', context)

def name(request, monkey_name):

    return HttpResponse(monkey_name)