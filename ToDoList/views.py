from django.shortcuts import render,redirect
from .models import ToDoList


def todolist(request):
    todolist = ToDoList.objects.all()
    return render(request, 'list.html', {'todolist' : todolist})

def createtodolist(request):
    author = request.POST['txtAuthor']
    title = request.POST['txtTitle']
    description = request.POST['txtDescription']

    todolist = ToDoList.objects.create(author = author, title = title, description = description)

    return redirect('/to-do-list/')

def deletetodolist(request, id):
    todolist = ToDoList.objects.get(id = id)
    todolist.delete()

    return redirect('/to-do-list/')

