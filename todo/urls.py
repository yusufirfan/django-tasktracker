from django.urls import path, include

from .views import (
    # FBV:
    todo_list,
    todo_add,
    todo_update,
    todo_delete,
)

# after '/':
urlpatterns = [
    path('list/', todo_list, name='list'),
    path('add/', todo_add, name='add'),
    path('update/<int:pk>', todo_update, name='todo_update'),
    path('delete/<int:pk>', todo_delete, name='todo_delete'),
]