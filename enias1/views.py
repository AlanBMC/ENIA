from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Pagina, CaixaTextos


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            try:
                pagina = Pagina.objects.get(usuario=usuario)
                return redirect('paginas', id_pagina=pagina.id)
            except Pagina.DoesNotExist:
                return render(request, 'login.html',  {'erro': 'Usuario ou Pagina nao existe'})
        except Usuario.DoesNotExist:
            return redirect('registro')
    else:
        return render(request, 'login.html')


def pagina(request, id_pagina):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        pagina = Pagina.objects.get(id=id_pagina)
        caixaT = CaixaTextos(pagina=pagina, texto=texto)
        caixaT.save()
        return redirect('paginas', id_pagina=id_pagina)
    else:
        pagina = Pagina.objects.get(id=id_pagina)
        lista_caixatextos = CaixaTextos.objects.filter(
            pagina=pagina).order_by('-datahora')
        usuario = Usuario.objects.get(id=pagina.id)
        print(usuario.nome)
        return render(request, "pagina.html", {"pagina": usuario.nome, "lista_caixatextos": lista_caixatextos})


def registro(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('nome')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')
        email = request.POST.get('email')

        # Validar se as senhas são iguais
        if senha1 != senha2:
            return render(request, "registro.html", {'erro': 'As senhas devem ser iguais!'})
        else:            # Criar o usuário no banco de dados

            usuario = Usuario(nome=nome_usuario, senha=senha1, email=email)
            if not Usuario.objects.filter(email=email).exists():
                usuario.save()
                pagina = Pagina(titulo=usuario.nome, usuario=usuario)
                pagina.save()
                print('que que TA ACONTECENDO')
                return redirect('login')
            else:

                return render(request, 'registro.html', {'erro': 'email ja cadastrado'})
    else:
        return render(request, "registro.html", {'erro': '?????'})
