from django.shortcuts import render
from projects.forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'projects/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True   
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'projects/registration.html',
                                                {'user_form':user_form,
                                                'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone failed to login")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse('Invalid login details')
    else:
        return render(request, 'projects/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_projects(request):
    return render(request, 'projects/projects.html')
