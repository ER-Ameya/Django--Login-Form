from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        userName = form.clean_data['userName']
        passWord = form.clean_data['passWord']
        user = authenticate(request, username=userName, password=passWord)
        if user is not None:
            login(request,user)
            return redirect('home')
        
    return render(request, 'templates\login.html', {'form': form})

def home(request):
    return render(request, "myapp/index.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.firstname = firstname
        myuser.lastname = lastname
        
        myuser.save()
        
        messages.success(request, "User has been created successfully")
        return redirect('signin')
    
    return render(request, "myapp/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username = username, password =  pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name 
            return render(request, "myapp/index.html", {fname:fname})
            
        else:
            messages.error(request, "Invalid User Details")
            return redirect('home')
        
        
        
    return render(request, "myapp/signin.html")

def signout(request):
    pass

