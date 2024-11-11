from django.shortcuts import render, redirect
from django.views import generic
from .models import User, TODOO
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        fnm = request.POST['fnm']
        email_id = request.POST['email']
        pwd = request.POST['pwd']
        print(f"this is our fnm: {fnm} our email_id {email_id} and our pwd {pwd}")
        my_user = User.objects.create_user(fnm, email_id, pwd)
        my_user.save()
        return redirect('/loginn')
    return render(request, 'todo/signup.html')


def loginn(request):
    if request.method == 'POST':
        fnm = request.POST['fnm']
        pwd = request.POST['pwd']
        print(f"this is our fnm: {fnm} and our pwd {pwd}")
        userr = authenticate(request, username=fnm, password=pwd)
        if userr:
            login(request, user=userr)
            return redirect('/todo')
        else:
            return redirect('/loginn')
    return render(request, 'todo/login.html')


def todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        print(title)
        obj = TODOO(title=title, user=request.user)
        obj.save()
        res = TODOO.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo', {'res': res})
    res = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo/todo.html', {'res': res})


def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST['title']
        print(title)
        obj = TODOO.objects.get(srno=srno)
        obj.title = title
        res = TODOO.objects.get(srno=srno)
        return redirect('/todo', {'res': res})
    res = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo/todo.html', {'res': res})