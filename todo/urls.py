from django.urls import path, include

# from .views import (
#     # FBV:
#     todo_list,
#     todo_add,
#     todo_update,
#     todo_delete,
#     TodoListView,
    
# )

from .views import *


# after '/':
urlpatterns = [
    # path('list/', todo_list, name='list'),
    # path('add/', todo_add, name='add'),
    # path('update/<int:pk>', todo_update, name='todo_update'),
    # path('delete/<int:pk>', todo_delete, name='todo_delete'),
    path('list/', TodoListView.as_view(), name='todo_list'),
    path('add/', TodoCreateView.as_view(), name='todo_add'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name="todo_update"),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name="todo_delete"),
]
