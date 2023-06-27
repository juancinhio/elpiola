from django.http import HttpResponse
#from django.template import Context,Template#
from django.shortcuts import render

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def saludo_vista(request):
	return HttpResponse("<h1>vistas<h1>")

def nombres(request, nombre :str, apellido :str):
	nombre = nombre
	apellido = apellido
	return HttpResponse(f"{apellido},{nombre}")    

def probando(request):
	nombre = "roberto"
	apellido = "carlos"
	datos = {"nombre" : nombre, "apellido": apellido}
	return render(request,"template1.html", context = datos)


def hora(request):
	from datetime import datetime

	hora = datetime.now()
	return HttpResponse(f"fecha y hora {hora}")

def notas(request):
	lista = [1,2,3,4,5,6,7,8,9]
	contexto = {"lista": lista}
	return render(request, "notas.html", contexto)