from django.urls import path
from . import views


urlpatterns = [
    path("cadastro_vagas/", views.criar_vaga, name='criar_vaga'),
    path('<int:vaga_id>', views.inscricao_vaga, name='inscricao')
]