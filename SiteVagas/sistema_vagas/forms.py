from django import forms
from dashboard.models import escolaridades, faixa_salarial


class CriarVaga(forms.Form):

    nome_vaga = forms.CharField(max_length=50)

    salario = forms.ChoiceField(choices=faixa_salarial)

    requisitos = forms.CharField(widget=forms.Textarea(attrs={'name': 'requisitos', 'rows': 3, 'cols': 5}))

    escolaridade_minima = forms.ChoiceField(choices=escolaridades)


class InscreverVaga(forms.Form):

    salario = forms.ChoiceField(choices=faixa_salarial)

    experiencia = forms.CharField(widget=forms.Textarea(attrs={'name': 'experiencia', 'rows': 10, 'cols': 50}))

    ultima_escolaridade = forms.ChoiceField(choices=escolaridades)

