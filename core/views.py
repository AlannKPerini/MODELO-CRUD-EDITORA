from django.shortcuts import render, redirect, get_object_or_404

from core.forms import AutorForm, ClienteForm
from core.models import Autor
from core.models import Cliente

def home(request):
    return render(request, 'portal/home.html')

def autor(request):
    autores = Autor.objects.all()  # crio a variável autores
    context = {  # criar dicionário de dados para receber valores e passo essa variável autores para o template
        'autores': autores
    }
    return render(request, 'portal/autor.html', context)

# FUNÇÃO PARA ADICIONAR AUTOR
def autor_add(request):
    form = AutorForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')
    context = {
        'form': form
    }
    return render(request, 'portal/autor_add.html', context)

# FUNÇÃO PARA EDITAR AUTOR
def autor_edit(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    form = AutorForm(request.POST or None, instance=autor)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')
    context = {
        'form': form,
        'autor': autor.id
    }
    return render(request, 'portal/autor_edit.html', context)

# FUNÇÃO PARA EXCLUIR AUTOR
def autor_delete(request, autor_pk):
    # autor = Autor.objects.get(pk=autor_pk)
    autor = get_object_or_404(Autor, pk=autor_pk)
    try:
        autor.delete()
        return redirect('autor')
    except:
        context = {
        }
    return render(request, 'autor', context)


def cliente(request):
    clientes = Cliente.objects.all()  # crio a variável clientes
    context = {  
        # criar dicionário de dados para receber 
        # valores e passo essa variável cliente para o template
        'clientes': clientes
    }
    return render(request, 'portal/cliente.html', context)


# FUNÇÃO PARA ADCIONAR CLIENTE
def cliente_add(request):
    form = ClienteForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cliente')
    context = {
        'form': form
    }
    return render(request, 'portal/cliente_add.html', context)

    # FUNÇÃO PARA EDITAR CLIENTE
def cliente_edit(request, cliente_pk):
    cliente = Cliente.objects.get(pk=cliente_pk)
    form = ClienteForm(request.POST or None, instance = cliente)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cliente')
    context = {
        'form': form,
        'cliente': cliente.id
    }
    return render(request,'portal/cliente_edit.html',context)

# FUNÇÃO PARA EXCLUIR CLIENTE
def cliente_delete(request, cliente_pk):
   
    cliente = get_object_or_404(Cliente, pk=cliente_pk)
    try:
        cliente.delete()
        return redirect('cliente')
    except:
        context = {
        }
    return render(request, 'cliente', context)