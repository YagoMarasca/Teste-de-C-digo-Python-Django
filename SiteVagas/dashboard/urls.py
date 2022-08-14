from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:vaga_id>", views.pag_vaga, name='pag_vaga'),
    path("relatorio/<int:vaga_id>", views.candidatos_inscritos, name='candidatos_inscritos')
]