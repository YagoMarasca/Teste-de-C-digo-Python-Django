from django.shortcuts import render, get_object_or_404
from .models import Vaga, InscricoesVagas
from django.http import HttpResponse


def index(request):

    vagas = Vaga.objects.all()

    dados = {
        'vagas': vagas
    }

    return render(request, 'dashboard.html', dados)


def pag_vaga(request, vaga_id):

    vaga = get_object_or_404(Vaga, pk=vaga_id)

    dados = {'vaga': vaga}

    return render(request, 'vaga.html', dados)


def candidatos_inscritos(request, vaga_id):

    vagas = InscricoesVagas.objects.filter(vaga_id=vaga_id).all()

    dados = {
        'vagas': vagas
    }

    return render(request, 'relatorio.html', dados)








