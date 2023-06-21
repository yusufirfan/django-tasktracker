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

def todo_update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method== "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Güncellendi.')
            return redirect("index")
    return render(request, 'update.html', {
        'form': form,
        'todo': todo
    })

def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    messages.success(request, 'Silindi.')
    return redirect("index")