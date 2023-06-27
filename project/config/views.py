from django.http import HttpResponse
from django.template import Context,Template

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def saludo_vista(request):
	return HttpResponse("<h1>vistas<h1>")

def nombres(request, nombre :str, apellido :str):
	nombre = nombre
	apellido = apellido
	return HttpResponse(f"{apellido},{nombre}")    

def probando(request):
	mi_html = open("./templates/template1.html", encoding="utf-8")
	mi_template = Template(mi_html.read())
	mi_html.close()
	mi_contexto = Context()
	mi_documento = mi_template.render(mi_contexto)
	return HttpResponse(mi_documento)