from django.shortcuts import render,redirect
from .models import Room,Message,Topic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import RoomForm,MessageForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse

def loginPage(request):
    if(request.user.is_authenticated): return redirect('home')
    page="log"
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
    return render(request,'base/login.html',{'pagetype':page})

def registerPage(request):
    if(request.user.is_authenticated): return redirect('home')
    page="reg"
    form=UserCreationForm()
    if(request.method=="POST"):
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            user=form.save(commit=False)
            user.username.strip()
            user.password.strip()
            user.save()
            login(request,user)
            return redirect('home')
        else : messages.error(request,"An error occured during registration")
            
    context={'pagetype':page,'form':form}
    return render(request,'base/login.html',context)

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

@login_required(login_url='login')
def room(request,pk):
    myroom=Room.objects.get(id=pk)
    chats=myroom.message_set.all()
    participants=myroom.participants.all()
    roomsize=participants.count()
    if(request.method=="POST"):
        body=request.POST.get('comment').strip()
        if(len(body)>0):
            message=Message.objects.create(
            room=myroom,
            user=request.user,
            body=body,
            )
            myroom.participants.add(message.user)
            return redirect('room',pk=pk)
    context={'myroom':myroom,'roomchats':chats, 'participants':participants,'roomsize':roomsize}
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
def deleteroom(request,pk):
    room=Room.objects.get(id=pk)
    if(room.host!=request.user): return HttpResponse("Not Authorized")
    if(request.method=="POST"):
        room.delete()
        return redirect('my-room',user=room.host.username)
    return render(request,'base/delete.html',{'obj':room})

@login_required(login_url='login')
def deletemessage(request,pk):
    message=Message.objects.get(id=pk)
    if(message.user!=request.user): return HttpResponse("Not Authorized")
    if(request.method=="POST"):
        message.delete()
        return redirect('room',pk=message.room.id)
    return render(request,'base/delete.html',{'obj':message})

@login_required(login_url='login')
def editmessage(request,pk):
    message=Message.objects.get(id=pk)
    if(message.user!=request.user): return HttpResponse("Not Authorized")
    form=MessageForm(instance=message)
    if(request.method=="POST"):
        form=MessageForm(request.POST,instance=message)
        if(form.is_valid()):
            form.save()
            return redirect('room',pk=message.room.id)
    return render(request,'base/editmessage.html',{'form':form})

