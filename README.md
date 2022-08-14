# Teste-de-C-digo-Python-Django

Enunciado: 
Objetivo: Criar um sistema usando 3.4+ e Django 2.2+.

Considere dois usuários. Obrigatório o cadastro com email (username = email) e senha.

Empresa deve criar uma (ou várias) vagas.
Candidato deve se candidatar a uma (ou mais) vagas.
A vaga que a empresa vai criar deve ter:

Nome da vaga
Faixa salarial:
Até 1.000
De 1.000 a 2.000
De 2.000 a 3.000
Acima de 3.000
Requisitos
Escolaridade mínima:
Ensino fundamental
Ensino médio
Tecnólogo
Ensino Superior
Pós / MBA / Mestrado
Doutorado
O candidato deve informar:

Pretensão salarial
Experiência
Última Escolaridade
Objetivo:

Tela de vagas com número de candidatos
Ser possível acessar quais candidatos (todos os dados) estão na vaga
Considere que a empresa tem o poder de editar ou deletar as vagas.


Funcionamento: 

Não foram implementados static files no projeto (sem CSS).

O sistema foi produzido dentro de um ambiente anaconda, com python 3.6.13 e Django 3.2.15.
Além disso, foi utilziado o PostgreSQL na implementação da DataBase.

- APPS:

Dashboard: App responsável pela página principal, realiza a verificação do tipo de usuários, apresenta todas as vagas cadastradas.

sistema_vagas: sistema de criação de vagas.

usuarios: sistema de criação de usuários.


- Descrição do site:

Ao abrir o site, a primeira página é o dashboard, onde já apresenta algumas vagas. Na tela também há alguns botões, para cadastro/login/logout de usuários. 
para uma pessoa poder se inscrever em uma vaga, é necessário criar um usuário (que não represente uma empresa) e depois realizar o login.

Para uma empresa criar uma vaga, basta também se cadastrar (informar que representa uma empresa) e fazer login. irá aparecer um novo botão para realizar a criação
das vagas. 

Toda empresa que criar uma vaga, poderá verificar todos os usuários que se inscreveram para a vaga. Tendo as suas informações presentes dentro de uma tabela.
Para acessar esta tabela, basta entrar dentro da vaga que deseja verificar e irá aparecer um botão que irá direcionar para esta página de informações.
Esta funcionalidade só está disponível para a empresa que criou a vaga.

