from django.shortcuts import render,redirect
from .models import Room,Message,Topic
from django.contrib.auth.models import User
from .forms import RoomForm

def home(request):
    allroom=Room.objects.all()
    context={'rooms':allroom}
    return render(request,'base/home.html',context)


def room(request,pk):
    myroom=Room.objects.get(id=pk)
    chats=Message.objects.filter(room=myroom.id)
    context={'myroom':myroom,'roomchats':chats}
    return render(request,'base/room.html',context)
    
def create_room(request):
    form=RoomForm()
    if(request.method=='POST'):
        form=RoomForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)

def my_room(request,user):
    getuser=User.objects.get(username=user)
    myrooms=Room.objects.filter(host=getuser)
    context={'myrooms':myrooms}
    return render(request,'base/myroom.html',context)

def update_room(request,pk):
    getroom=Room.objects.get(id=pk)
    form=RoomForm(instance=getroom)
    context={'form':form}
    return render(request,'base/room_form.html',context)
