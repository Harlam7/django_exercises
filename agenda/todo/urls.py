from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('view/<int:id>', views.view, name='todo_view'),  # Corregido a <int:id>
    path('edit/<int:id>', views.edit, name='todo_edit'),  # Corregido a <int:id>
    path('create/', views.create, name='todo_create'),    # Corregido 'create' a 'name'
    path('delete/<int:id>', views.delete, name='todo_delete')    # Corregido 'create' a 'name'
]
