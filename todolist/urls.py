from django.urls import path
from .views import *

app_name = 'todolist'

urlpatterns = [
    # path('', todolist, name='todolist'),
    path('login/', login_user, name='login_user'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('json/', todolist_ajax, name='todolist_ajax'),
    path('', todolist_ajax_html, name='todolist_ajax_html'),
    path('add/', create_task_ajax, name='create_task_ajax'),
]