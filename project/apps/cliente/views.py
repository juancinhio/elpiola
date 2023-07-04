from django.shortcuts import render

# Create your views here.
from .models import Cliente

def index(request):
    clientes_registros = Cliente.objects.all()
    return render(request, "index.html",{"clientes":clientes_registros})