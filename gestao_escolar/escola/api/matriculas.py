from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Count
from django.http import JsonResponse
from django.db import connection


from escola.models import Matricula, Aluno, Curso
from escola.serializers import MatriculaSerializer, AlunoSerializer, CursoSerializer

class MatriculaList(APIView):
    def get(self, request):
        matriculas = Matricula.objects.all()
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MatriculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class MatriculaDetail(APIView):
    def get(self, request, pk):
        matricula = Matricula.objects.get(pk=pk)
        serializer = MatriculaSerializer(matricula)
        return Response(serializer.data)

    def put(self, request, pk):
        matricula = Matricula.objects.get(pk=pk)
        serializer = MatriculaSerializer(matricula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        matricula = Matricula.objects.get(pk=pk)
        matricula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MatriculaPagar(APIView):
    def post(self, request, pk):
        matricula = Matricula.objects.get(pk=pk)
        matricula.status = 'PAGO'
        matricula.save()
        return Response({'status': 'Matrícula marcada como paga'})


class MatriculaPendencias(APIView):
    def get(self, request):
        pendentes = Matricula.objects.filter(status='PENDENTE')
        total = sum(m.curso.valor_inscricao for m in pendentes)

        return Response({
            "total_matriculas_pendentes": pendentes.count(),
            "valor_total_pendente": float(total)
        })
class TotalMatriculasPorCurso(APIView):
    def get(self, request):
        dados = (
            Curso.objects
            .annotate(total_matriculas=Count('matriculas'))
            .values('id', 'nome', 'total_matriculas')
        )

        return Response(list(dados))
    
def matriculas_por_curso(request):

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.nome AS curso,
                   COUNT(m.id) AS total_matriculas
            FROM escola_curso c
            LEFT JOIN escola_matricula m ON m.curso_id = c.id
            GROUP BY c.nome
            ORDER BY c.nome;
        """)
        dados = cursor.fetchall()

    # dados fica assim: [('ADS', 10), ('TI', 5)]

    return JsonResponse({
        "resultados": [
            {"curso": row[0], "total_matriculas": row[1]} 
            for row in dados
        ]
    })