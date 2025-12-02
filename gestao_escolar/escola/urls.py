from rest_framework.routers import DefaultRouter
from core.views import AlunoViewSet, CursoViewSet, MatriculaViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
