from rest_framework import serializers
from .models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'cpf', 'data_ingresso']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'carga_horaria', 'valor_inscricao', 'status']


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'data_matricula', 'status', 'aluno', 'curso']
