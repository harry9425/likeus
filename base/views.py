from django.shortcuts import render
from .models import Room

def home(request):
    allroom=Room.objects.all()
    context={'rooms':allroom}
    return render(request,'base/home.html',context)


def room(request,pk):
    myroom=Room.objects.get(id=pk)
    context={'myroom':myroom}
    return render(request,'base/room.html',context)
    
