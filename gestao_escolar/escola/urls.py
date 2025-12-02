from rest_framework.routers import DefaultRouter
from escola.views import AlunoViewSet, CursoViewSet, MatriculaViewSet
from django.urls import path, include
from . import views

rota = DefaultRouter()
rota.register(r'alunos', AlunoViewSet)
rota.register(r'cursos', CursoViewSet)
rota.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('api/', include(rota.urls)),
    path('', views.home, name='home'),
]
