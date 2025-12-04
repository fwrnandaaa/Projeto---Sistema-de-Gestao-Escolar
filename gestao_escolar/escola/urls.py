from django.contrib import admin
from django.urls import path, include
from escola import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('escola.api.urls')),

    path('', views.home, name='home'),
    path('alunos/', views.alunos, name='alunos'),
    path('cursos/', views.cursos, name='cursos'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('alunos/cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cursos/cadastrar/', views.cadastrar_curso, name='cadastrar_curso'),

]
