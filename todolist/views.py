from multiprocessing import context
from urllib import response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from todolist.models import Task
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:todolist_ajax_html")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response

        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def todolist(request):
    # data_todolist = Task.objects.filter(user = request.user)
    data_todolist = Task.objects.all()
    user_todolist = []
    name = request.user.username
    for data in data_todolist:
        if data.user.username == name:
            user_todolist.append(data)
    context = {
        'username': name,
        'user_todolist': user_todolist,
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    user = request.user
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(user=user, date=datetime.date.today(), title=title, description=description)
        response = HttpResponseRedirect(reverse('todolist:todolist'))
        return response

    context = {}
    return render(request, 'create-task.html', context)

def todolist_ajax(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def todolist_ajax_html(request):
    name = request.user.username
    context = {
        'username': name
    }
    return render(request, 'ajax-todolist.html', context)

@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task_ajax(request):
    user = request.user
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        result = Task.objects.create(user=user, date=datetime.date.today(), title=title, description=description)
        print(result)
        result_dict = {"title":result.title,"date":datetime.date.today(),"description":result.description}
        return JsonResponse(result_dict)