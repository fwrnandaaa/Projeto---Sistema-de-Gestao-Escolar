from rest_framework.routers import DefaultRouter
from core.views import AlunoViewSet, CursoViewSet, MatriculaViewSet

rota = DefaultRouter()
rota.register(r'alunos', AlunoViewSet)
rota.register(r'cursos', CursoViewSet)
rota.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('api/', include(rota.urls)),
]
