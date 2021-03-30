from django.contrib.auth import authenticate, login
from django.forms.forms import Form
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@login_required
def index(request):
    return render(request,'dashboard.html')


def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')

    else:
        form = UserCreationForm()        
    

    context = {'form':form}
    return render(request,'registration/register.html',context)