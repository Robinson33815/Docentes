from django.shortcuts import render, redirect, get_object_or_404
from .models import Docente
from .forms import DocenteForm

def lista_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes/lista.html', {'docentes': docentes})

def crear_docente(request):
    form = DocenteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_docentes')
    return render(request, 'docentes/formulario.html', {'form': form, 'titulo': 'Crear Docente'})

def editar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    form = DocenteForm(request.POST or None, request.FILES or None, instance=docente)
    if form.is_valid():
        form.save()
        return redirect('lista_docentes')
    return render(request, 'docentes/formulario.html', {'form': form, 'titulo': 'Editar Docente'})

def eliminar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.delete()
        return redirect('lista_docentes')
    return render(request, 'docentes/eliminar.html', {'docente': docente})
