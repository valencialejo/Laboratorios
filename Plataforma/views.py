from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from Plataforma.models import *
from django.db.models import Sum

logger = logging.getLogger(__name__)

def ventas(request):
    ventas=Venta.objects.all()
    usuarios=Usuario.objects.all()

    max=0
    usuario_max=''
    for u in usuarios:
        for i in ventas:
            precio=Venta.objects.filter(user=u.id).aggregate(Sum('precio_t'))
        preciot=precio['precio_t__sum']
        if preciot>max:
            max=preciot
            usuario_max=u.usuario
        
    data={
        'ventas':ventas,
        'usuario_max':usuario_max,
        'max_ventas':max,
    }
    return render(request,"ventas.html",data)

def principal(request):
    return render(request,'principal.html')


def publicaciones(request):
    publicaciones=Publicacion.objects.all()
    autores=Usuario.objects.all()
    data={
        'usuario':request.user.username,
        'publicaciones':publicaciones,
        'autores':autores,
    }
    return render(request,'publicaciones.html',data)

def login_request(request):

    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['psw']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout_request(request):
    print("Log out the user `{}`".format(request.user.username))
    logout(request)
    return redirect('/')

def registro_request(request):

    context = {}
    if request.method == 'GET':
        return render(request, 'registro.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            usuario=Usuario.objects.create(nombre=first_name,apellidos=last_name,usuario=username,contraseña=password)
            login(request, user)
            return redirect("/")
        else:
            context['message'] = "User already exists."
            return render(request, 'registro.html', context)

def add_pub(request,user_id):

    if request.method=="GET":
        return render(request,'añadir_publicacion.html')
    else:
        contenido=request.POST['contenido']
        usuario_id=User.objects.filter(pk=user_id).get()
        publicacion=Publicacion.objects.create(contenido=contenido,user=usuario_id)
        return redirect("/")