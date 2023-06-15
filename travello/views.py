from django.shortcuts import render
from .models import Destination
from .serializers import DestinationSerializer
from django.http import JsonResponse


# Create your views here.

def index(request):

    # static data 
    # dest1=Destination()
    # dest1.name="Bangalore"
    # dest1.desc='Beautiful Weather, Beautiful City'
    # dest1.img='destination_1.jpg'
    # dest1.price=850
    # dest1.offer=True

    # dest2=Destination()
    # dest2.name="Hyderabad"
    # dest2.desc='First Biryani then Work'
    # dest2.img='destination_2.jpg'
    # dest2.price=800
    # dest2.offer=False

    # dest3=Destination()
    # dest3.name="Noida"
    # dest3.desc='Explore and Enjoy'
    # dest3.img='destination_3.jpg'
    # dest3.price=750
    # dest3.offer=False
    # dests = [dest1, dest2, dest3]

    # dynamic data 
    dests=Destination.objects.all()

    return render(request, 'index.html', {'dests':dests})

# single destination 
def destination_details(request, pk):
    dest=Destination.objects.get(id=pk)
    serializer=DestinationSerializer(dest)
    return JsonResponse(serializer.data)

# all destinations together 
def destinations(request):
    dest=Destination.objects.all()
    serializer=DestinationSerializer(dest, many=True)
    return JsonResponse(serializer.data, safe=False)
