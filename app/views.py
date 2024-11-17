from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import reserva
from app.forms import AgendaForm 

def home(request):
    return render(request, 'index.html')

def ambiente(request):
    return render(request, 'ambientes.html')

def planos(request):
    agenda = reserva.objects.all()
    return render(request, 'planos.html', {'agenda' : agenda})


def agenda(request):
    form = AgendaForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('planos')

    dados_form = {
        'form' : form
    }

    return render(request, 'agenda.html', dados_form)



def agenda_del(request, reserva_pk):
    data_pos = reserva.objects.get(pk=reserva_pk)
    data_pos.delete()

    return redirect('menu_agendamento')