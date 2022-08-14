from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from django.contrib import auth


def cadastro(request):
    if request.method == 'POST':
        email = request.POST["email"]
        senha = request.POST["password"]
        tipo_user = request.POST.get("tipo_usuario", False)
        user = User.objects.create_user(username=email, password=senha)
        user.save()
        print(request.POST)
        if tipo_user == 'on':
            assign_role(user, 'empresa')
        else:
            assign_role(user, 'candidato')
        return redirect('index')

    return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['usuario']
        senha = request.POST['senha']

        if email.split() == '' or senha.split() == '':
            return redirect('login')

        elif User.objects.filter(username=email).exists():
            user = auth.authenticate(request, username=email, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect('index')

    return render(request, 'login.html')




def logout(request):
    auth.logout(request)
    return redirect('index')

