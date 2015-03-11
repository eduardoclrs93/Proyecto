from django.shortcuts import render
from login.models import Usuario

# Create your views here.

def MostrarUsuarios(request):
	users = Usuario.objects.all()
	return render(request, 'login/muestra.html', {'users': users})