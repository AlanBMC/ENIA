from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Usuario, Pagina, Caixa_de_texto
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def pagina(request, id_pagina, username):
    try:
        pagina =Pagina.objects.get(id=id_pagina)
    except Pagina.DoesNotExist:
        return HttpResponse("Erro 404")
    
    return render(request, 'usuarios.html', {'pagina': pagina, 'username':username})
   
    
def login(request):
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('pass')

        pagina_usuario = Pagina(titulo='PaginaDo-'+ username)
        pagina_usuario.save()
        novo_usuario = Usuario(nome=username, senha=password, pagina=pagina_usuario)
        novo_usuario.save()
        return redirect(reverse('nova_pagina', args=(pagina_usuario.id, username)))
    else:
        return render(request, 'login.html')
    

@login_required
def salva_texto(request):
    if request.method == "POST":
        id_pagina = request.POST.get('id_pagina')
        username = request.POST.get('username')
        texto = request.POST.get('texto')
        pagina = get_object_or_404(Pagina, id=id_pagina)
        usuario = get_object_or_404(Usuario, nome=username)
        #Verificar se o usuario é dono da pagina
        if(usuario == username):
            novo_texto = Caixa_de_texto(textos=texto, id_pg=pagina)
            novo_texto.save()
            return redirect(''  )

        else:
            return HttpResponseForbidden("Você não tem permissão para isso!")
