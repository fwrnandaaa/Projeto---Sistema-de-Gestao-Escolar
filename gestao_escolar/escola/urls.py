from django.contrib import admin
from django.urls import path, include
from escola import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('escola.api.urls')),

    path('', views.home, name='home'),
    path('alunos/', views.alunos, name='alunos'),
    path("alunos/editar/<str:cpf>/", views.editar_aluno, name="editar_aluno"),
    path("alunos/deletar/<str:cpf>/", views.deletar_aluno, name="deletar_aluno"),
    path("cursos/", views.cursos, name="cursos"),
    path("cursos/editar/<int:id>/", views.editar_curso, name="editar_curso"),
    path("cursos/deletar/<int:id>/", views.deletar_curso, name="deletar_curso"),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('alunos/cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cursos/cadastrar/', views.cadastrar_curso, name='cadastrar_curso'),

]
