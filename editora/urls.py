from django.contrib import admin
from django.urls import path
# da minha própria view importa as views
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/add/', views.autor_add, name='autor_add'),
    path('autor/', views.autor, name='autor'),
    path('autor/edit/<int:autor_pk>', views.autor_edit, name='autor_edit'),
    path('autor/delete/<int:autor_pk>', views.autor_delete, name='autor_delete'),
    
    # url dos clientes
    path('', views.home, name='home'),
    path('cliente/', views.cliente, name='cliente'),
    path('cliente/add/', views.cliente_add, name='cliente_add'),
    path('cliente/edit/<int:cliente_pk>', views.cliente_edit, name = 'cliente_edit'),
    path('cliente/delete/<int:cliente_pk>', views.cliente_delete, name = 'cliente_delete'),


    #  path('dashboard/', views.dashboard, name='dashboard'),
    #  path('editora/', views.editora, name='editora'),
    #  path('livro/', views.livro, name='livro'),
    #  path('formato/', views.formato, name='formato')
]