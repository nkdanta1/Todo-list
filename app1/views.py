from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from.models import Todo
# Create your views here.

def insert_todo_item(request : HttpRequest):
    content = request.POST['content']
    todo = Todo(content=content)
    todo.save()
    return redirect('/')


def list_todo_items(request):
        todo_list=Todo.objects.all()
        return render(request,'todo_list.html',{'todo_list':todo_list})

def delete_todo_item(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')