from django.db import models
from datetime import datetime,date
from django.core.exceptions import ValidationError

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    cpf = models.CharField(max_length=11, unique=True)
    data_ingresso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Aluno: {self.nome} - Email: {self.email} - CPF: {self.cpf} - Data de ingresso: {self.data_ingresso}'

    def clean(self):
        erros = {}
        if len(self.nome) < 10:
            erros['nome']='O nome completo deve ter pelo menos 10 caracteres.'
        if len(self.cpf)!=11 or not self.cpf.isdigit():
            erros['cpf']='O CPF deve conter 11 dígitos numéricos.'
        if len(self.email) < 6:
            erros['email'] = 'Email muito curto.'
        if erros:
            raise ValidationError(erros)
        
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    valor_inscricao = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20,choices=[('ATIVO','Ativo'),('INATIVO','Inativo')],default='ATIVO')

    def __str__(self):
        s = f'Nome do curso: {self.nome} - Carga horária: {self.carga_horaria} - '
        s+= f'Valor da inscrição: {self.valor_inscricao} - Status: {self.status}'
        return s

    def clean(self):
        erros = {}
        if len(self.nome) < 10:
            erros['nome']='O nome do curso deve ter pelo menos 10 caracteres.'
        if self.carga_horaria < 1:
            erros['carga_horaria']='A carga horária do curso não pode ser negativa.'
        if self.valor_inscricao < 0:
            erros['valor_inscricao'] = 'O valor da inscrição não pode ser negativo.'
        if erros:
            raise ValidationError(erros)

class Matricula(models.Model):
    data_matricula = models.DateField(default=date.today)
    status = models.CharField(max_length=20,choices=[('PAGO','Pago'),('PENDENTE','Pendente')],default='PENDENTE')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')

    curso = models.ForeignKey(Curso,on_delete=models.CASCADE, related_name='matriculas')

    def __str__(self):
        s = f'Aluno: {self.aluno.nome} - Curso: {self.curso.nome} - '
        s+= f'Data da matrícula: {self.data_matricula} - Status: {self.status}'
        return s