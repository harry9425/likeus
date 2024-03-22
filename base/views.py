from django.shortcuts import render

rooms=[
    {'id':1, 'name':'Learn Django'},
    {'id':2, 'name':'Python talks'},
    {'id':3, 'name':'Php Sucks'},
]

def home(request):
    context={'rooms':rooms}
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html')
    
