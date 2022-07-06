from django.contrib import admin
from django.urls import path
# da minha própria view importa as views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/add/', views.autor_add, name='autor_add'),
    path('autor/', views.autor, name='autor'),
    path('autor/edit/<int:autor_pk>', views.autor_edit, name='autor_edit'),
    path('autor/delete/<int:autor_pk>', views.autor_delete, name='autor_delete')
    #  path('dashboard/', views.dashboard, name='dashboard'),
    #  path('editora/', views.editora, name='editora'),
    #  path('livro/', views.livro, name='livro'),
    #  path('formato/', views.formato, name='formato')
]