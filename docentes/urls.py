from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_docentes, name='lista_docentes'),
    path('crear/', views.crear_docente, name='crear_docente'),
    path('editar/<int:pk>/', views.editar_docente, name='editar_docente'),
    path('eliminar/<int:pk>/', views.eliminar_docente, name='eliminar_docente'),
]
