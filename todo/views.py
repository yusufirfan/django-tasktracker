from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'list.html', context)

from django.contrib import messages
from django.shortcuts import redirect

def todo_add(request):
    # if request.POST:
    #     form = TodoForm(request.post)
    #     form.save()
    # else :
    #     form = TodoForm()

    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Added.')
        return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'add.html', context)