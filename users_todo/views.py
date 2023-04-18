from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .models import UsersTodoList
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from datetime import datetime


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        todoList=UsersTodoList.objects.filter(user_id=request.user.id, deleted_at__isnull=True).order_by('-on_priority', '-created_at', 'completed_at').values()
        completed_tasks_count=UsersTodoList.objects.filter(user_id=request.user.id, completed_at__isnull=False, deleted_at__isnull=True).count()
        priority_tasks_count=UsersTodoList.objects.filter(user_id=request.user.id, completed_at__isnull=True, on_priority=1, deleted_at__isnull=True).count()
        normal_tasks_count=UsersTodoList.objects.filter(user_id=request.user.id, completed_at__isnull=True, on_priority=0, deleted_at__isnull=True).count()
        context = {
            'user_full_name': request.user.first_name+' '+request.user.last_name, 
            'todos':todoList, 
            'completed_tasks_count': completed_tasks_count, 
            'priority_tasks_count': priority_tasks_count, 
            'normal_tasks_count': normal_tasks_count
            }
        return render(request, 'home.html', context)
    return redirect('login_view')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'signup.html')

def createAccount(request):
    validationFailed=0
    if not request.POST['first_name']:
        validationFailed=1
        messages.error(request, 'First Name is required!')
    if not request.POST['last_name']:
        validationFailed=1
        messages.error(request, 'Last Name is required!')
    try:
        validate_email(request.POST['email_address'])
    except ValidationError:
        validationFailed=1
        messages.error(request, "Email is not in Valid Format!")
    if not request.POST['password']:
        validationFailed=1
        messages.error(request, 'Password is required!')

    if validationFailed:
        return render(request, 'signup.html')
    
    if User.objects.filter(email=request.POST['email_address']).exists():
            messages.error(request, 'Email address is already registered.')
            return render(request, 'signup.html')

    user = User.objects.create_user(username=request.POST['email_address'], email=request.POST['email_address'], password=request.POST['password'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()

    messages.success(request, 'Your account has been created successfully!')
    return redirect('login_view')

def loginAccount(request):
    try:
        validate_email(request.POST['email_address'])
    except ValidationError:
        messages.error(request, "Email is not in Valid Format!")
    if not request.POST['password']:
        messages.error(request, "Password is required")

    user = authenticate(request, username=request.POST['email_address'], password=request.POST['password'])
    if user:
        auth_login(request, user)
        return redirect('home')
    
    messages.error(request, 'Invalid email or password.')
    return redirect('login_view')

def logoutAccount(request):
    auth_logout(request)
    return redirect('login_view')

def AddNewTodo(request):
    title=request.POST['title'];
    desc=request.POST['description'];
    priority=0
    if 'priority' in request.POST:
        priority = request.POST['priority']
    if not title or not desc:
        messages.error(request, "Title and Desc required to add new todo.")
        return redirect('home')
    newTodo=UsersTodoList(title=title,description=desc, user_id=request.user, created_at=datetime.now())
    newTodo.on_priority=priority
    newTodo.save()
    messages.success(request, "New Todo has been added successfully")
    return redirect('home')

def markCompleted(request, todo_id):
    if not todo_id:
        messages.error(request, "Select Todo to mark as completed")
    todo=UsersTodoList.objects.get(id=todo_id)
    todo.completed_at=datetime.now()
    todo.on_priority=0
    todo.save()
    messages.success(request, "'"+todo.title+"' Marked as Completed!")
    return redirect('home')

def enablePriority(request, todo_id):
    todo=UsersTodoList.objects.get(id=todo_id)
    todo.on_priority=1
    messages.success(request, "'"+todo.title+"' Set on Priority!")
    todo.save()
    return redirect('home')

def disablePriority(request, todo_id):
    todo=UsersTodoList.objects.get(id=todo_id)
    todo.on_priority=0
    messages.success(request, "'"+todo.title+"' removed from Priority!")
    todo.save()
    return redirect('home')

def deleteTodo(request, todo_id):
    todo=UsersTodoList.objects.get(id=todo_id)
    todo.deleted_at=datetime.now()
    messages.success(request, "'"+todo.title+"' has been Deleted!")
    todo.save()
    return redirect('home')
