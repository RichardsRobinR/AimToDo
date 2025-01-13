from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from todo.forms import TodoListForm
from todo.models import TodoList

# Create your views here.
def main_page(request):
    todoList = TodoList.objects.all().values()
    # if request.method == "POST":
    #     form = TodoListForm(request.POST)
    #     if form.is_valid():
    #         # print(form.cleaned_data)
    #         return redirect('main_page')

    data = {
        'todoList': todoList,
    }
    print(data)
    return render(request, 'main_page.html', data)

def add(request):
    title = request.POST['title']
    TodoList.objects.create(title=title,description="",isCompleted=False)
    return redirect('main_page')

def delete(request, id):
    todo = get_object_or_404(TodoList, pk=id)
    todo.delete()
    return redirect('main_page')


def update(request, id):
    todo = get_object_or_404(TodoList, pk=id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True

    todo.isCompleted = isCompleted
    todo.save()
    return redirect('main_page')
