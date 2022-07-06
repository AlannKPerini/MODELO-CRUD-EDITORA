from django.shortcuts import render, redirect, get_object_or_404

from core.forms import AutorForm
from core.models import Autor


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
