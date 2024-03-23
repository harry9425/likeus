from django.shortcuts import render,redirect
from .models import Room,Message,Topic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import RoomForm
from django.contrib import messages
from django.http import HttpResponse

def loginPage(request):
    
    if(request.user.is_authenticated): return redirect('home')
    
    if(request.method=="POST"):
        username=request.POST.get('username').strip()
        password=request.POST.get('password').strip()
        if(len(username) and len(password)):
            try:
                exists=User.objects.get(username=username)
                user=authenticate(request,username=username,password=password)
                if(user==None):
                    messages.warning(request, "Wrong credentials")
                else:
                    login(request,user)
                    #messages.success(request, "LoggedIn Successfully")
                    return redirect('home')
            except: messages.error(request, "User Don't Exist!!")
            
        else: messages.warning(request, "Fields is Empty!!!")  
    return render(request,'base/login.html',{})

def logoutPage(request):
    logout(request)
    return redirect('home')

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

@login_required(login_url='login')
def create_room(request):
    form=RoomForm()
    if(request.method=='POST'):
        form=RoomForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def my_room(request):
    user=request.user
    getuser=User.objects.get(username=user)
    myrooms=Room.objects.filter(host=getuser)
    context={'myrooms':myrooms}
    return render(request,'base/myroom.html',context)

@login_required(login_url='login')
def update_room(request,pk):
    getroom=Room.objects.get(id=pk)
    if(getroom.host!=request.user): return HttpResponse("Not Authorized")
    form=RoomForm(instance=getroom)
    context={'form':form}
    if(request.method=='POST'):
        form=RoomForm(request.POST,instance=getroom)
        if(form.is_valid()):
            form.save()
            return redirect('my-room',user=getroom.host.username)
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def delete(request,pk):
    room=Room.objects.get(id=pk)
    if(room.host!=request.user): return HttpResponse("Not Authorized")
    if(request.method=="POST"):
        room.delete()
        return redirect('my-room',user=room.host.username)
    return render(request,'base/delete.html',{'obj':room})
