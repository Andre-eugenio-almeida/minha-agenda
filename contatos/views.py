from django.shortcuts import render, redirect
from .models import Categoria, Contato
from .forms import FormContato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'content/index.html', {'contatos': contatos})

def detalhes(request, id_contato):
    contato = Contato.objects.get(id=id_contato)
    return render(request, 'content/detalhes.html', {'contato': contato})

def novo_contato(request):
    if request.method == 'POST':
        form = FormContato(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = FormContato()
    return render(request, 'content/novo_contato.html', {'form': form})

