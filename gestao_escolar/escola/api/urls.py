from django.urls import path

from .alunos import AlunoList, AlunoDetail, AlunoMatriculas, AlunoTotalDevido
from .cursos import CursoList, CursoDetail, CursoTotalMatriculas
from .matriculas import  (MatriculaList, MatriculaDetail, MatriculaPagar, 
                          MatriculaPendencias, TotalMatriculasPorCurso, matriculas_por_curso)

urlpatterns = [
    path('alunos/', AlunoList.as_view(), name='listar-alunos'),
    path('alunos/<int:pk>/', AlunoDetail.as_view(), name='detalhes-aluno'),
    path('alunos/<int:pk>/matriculas/', AlunoMatriculas.as_view(), name='matriculas-do-aluno'),
    path('alunos/<int:pk>/total-devido/', AlunoTotalDevido.as_view(), name='total-devido-aluno'),
    path('cursos/', CursoList.as_view(), name='listar-cursos'),
    path('cursos/<int:pk>/', CursoDetail.as_view(), name='detalhes-curso'),
    path('matriculas/', MatriculaList.as_view(), name='listar-matriculas'),
    path('matriculas/<int:pk>/', MatriculaDetail.as_view(), name='detalhes-matricula'),
    path('matriculas/<int:pk>/pagar/', MatriculaPagar.as_view(), name='pagar-matricula'),
    path('matriculas/pendentes/', MatriculaPendencias.as_view(), name='matriculas-pendentes'),
    path('relatorios/matriculas-por-curso/', TotalMatriculasPorCurso.as_view()),
    path('matriculas-por-curso/', matriculas_por_curso, name='matriculas_por_curso'),
   
]
