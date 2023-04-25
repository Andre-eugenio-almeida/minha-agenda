from django.shortcuts import render
from .models import Categoria, Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'content/index.html', {'contatos': contatos})
