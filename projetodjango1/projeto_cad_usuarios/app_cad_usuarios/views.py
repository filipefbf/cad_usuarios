from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #Salvando um novo usuário da tela no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos os usuários cadastrados em uma pagina html
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retonar os dados para a pagina html
    return render(request, 'usuarios/usuarios.html', usuarios)