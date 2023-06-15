from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data = {
        'title': "Home Page",
        "body": "Welcome to The HOMEPAGE",
        'cars': ['Mercedes', 'BMW', 'Audi', 'Ferrari'],
        'details':
            [{
                'name': 'vivek',
                'college': 'lpu'},
             {
                'name': 'gourav',
                'college': 'lpu'
            }
        ]


    }
    return render(request, "index.html", data)


def about(request):
    return HttpResponse("Hello")


def aboutYou(request, id):
    return HttpResponse(id)


def index(request):
    return render(request, 'index.html')


def add(request):
    s = int(request.POST.get('s'))
    t = int(request.POST.get('t'))
    return render(request, 'result.html', {'result': s+t})
