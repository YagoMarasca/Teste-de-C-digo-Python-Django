from django.shortcuts import render, get_object_or_404, redirect
from .forms import CriarVaga, InscreverVaga
from dashboard.models import Vaga, InscricoesVagas
from django.contrib.auth.models import User


# Create your views here.


def criar_vaga(request):
    if request.method == 'POST':
        nome_vaga = request.POST['nome_vaga']
        salario = request.POST['salario']
        requisitos = request.POST['requisitos']
        escolaridade = request.POST['escolaridade_minima']

        empresa = get_object_or_404(User, pk=request.user.id)

        vaga = Vaga.objects.create(nome_vaga=nome_vaga, salario=salario, requisitos=requisitos,
                                   escolaridade_minima=escolaridade, empresa=empresa)

        vaga.save()

        return redirect('index')

    form = CriarVaga()
    dados = {
        'form': form
    }
    return render(request, 'criar_vaga.html', dados)


def inscricao_vaga(request, vaga_id):
    if request.method == 'POST':
        vaga = get_object_or_404(Vaga, pk=vaga_id)
        candidato = get_object_or_404(User, pk=request.user.id)

        salario = request.POST['salario']
        experiencia = request.POST['experiencia']
        escolaridade = request.POST['ultima_escolaridade']

        inscricao = InscricoesVagas.objects.create(vaga=vaga, candidato=candidato,
                                                   pretensao_salarial=salario,
                                                   experiencia=experiencia,
                                                   ultima_escolaridade=escolaridade)

        inscricao.save()

        return redirect('index')

    form = InscreverVaga()

    dados = {
        'form': form,
    }

    return render(request, 'inscricao_vaga.html', dados)
