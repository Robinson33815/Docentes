from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'materias/lista.html', {'cursos': cursos})

def crear_curso(request):
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_cursos')
    return render(request, 'materias/formulario.html', {'form': form, 'titulo': 'Crear Curso'})

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, request.FILES or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('lista_cursos')
    return render(request, 'materias/formulario.html', {'form': form, 'titulo': 'Editar Curso'})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')
    return render(request, 'materias/eliminar.html', {'curso': curso})
