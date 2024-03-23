from django.shortcuts import render,redirect
from .models import Room,Message,Topic
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import RoomForm

def home(request):
    q=request.GET.get('q')
    allroom=Room.objects.filter(
        Q(topic__name__icontains=("" if q==None else q)) |
        Q(name__icontains=("" if q==None else q)) |
        Q(description__icontains=("" if q==None else q))
    )
    alltopics=Topic.objects.all()
    roomscount=len(allroom)
    context={'rooms':allroom,'topics':alltopics,'roomscount':roomscount}
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
    if(request.method=='POST'):
        form=RoomForm(request.POST,instance=getroom)
        if(form.is_valid()):
            form.save()
            return redirect('my-room',user=getroom.host.username)
    return render(request,'base/room_form.html',context)

def delete(request,pk):
    room=Room.objects.get(id=pk)
    if(request.method=="POST"):
        room.delete()
        return redirect('my-room',user=room.host.username)
    return render(request,'base/delete.html',{'obj':room})
