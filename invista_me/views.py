from django.shortcuts import render,redirect,HttpResponse
from .models import investimento
from .forms import InvestimentoForm


# Create your views here.
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


def editar(request, id_investimento):
    investiment = investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investiment)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investiment)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')


def excluir(request, id_investimento):
    investiment = investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investiment.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investiment})
        

    
def investimentos(request):
    dados = {
        'dados':investimento.objects.all()
    }
    return render(request,'investimentos/investimentos.html', context=dados)


def detalhe(request,id_investimento):
    dados = {
        'dados':investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)
    
