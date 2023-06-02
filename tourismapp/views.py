from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request,'gallery.html')

def place(request):
    return render(request,'place.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')