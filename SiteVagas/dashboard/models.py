from django.db import models
from django.contrib.auth.models import User

escolaridades = [
        ("Ensino Fundamental", "Ensino Fundamental"),
        ("Ensino Médio", "Ensino Médio"),
        ("Tecnólogo", "Tecnólogo"),
        ("Ensino Superior", "Ensino Superior"),
        ("Pós/MBA/Mestrado", "Pós/MBA/Mestrado"),
        ("Doutorado", "Doutorado")
    ]

faixa_salarial = [
    ("Até 1.000", "Até 1.000"),
    ("De 1.000 até 2.000", "De 1.000 até 2.000"),
    ("De 2.000 até 3.000", "De 2.000 até 3.000"),
    ("Acima de 3.000", "Acima de 3.000"),
]


class Vaga(models.Model):
    nome_vaga = models.CharField(max_length=50)

    empresa = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    salario = models.CharField(choices=faixa_salarial, max_length=20)

    requisitos = models.CharField(max_length=250)

    escolaridade_minima = models.CharField(choices=escolaridades, default="", max_length=19)


class InscricoesVagas(models.Model):

    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    candidato = models.ForeignKey(User, on_delete=models.PROTECT, default=None)

    pretensao_salarial = models.CharField(choices=faixa_salarial, max_length=20)

    experiencia = models.CharField(max_length=300)

    ultima_escolaridade = models.CharField(choices=escolaridades, max_length=19)



