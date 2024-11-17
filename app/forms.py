from django import forms
from .models import reserva

class AgendaForm(forms.ModelForm):
    class Meta:
        model = reserva
        exclude = ()

        widgets = {
            'rg_cliente' : forms.TextInput(attrs={'class': 'form-control', 'autofocus': "" }),
            'nome_cliente' : forms.TextInput(attrs={'class': 'form-control'}),
            'email_cliente' : forms.EmailInput(attrs={'class': 'form-control'}),
            #'data_inicio' : forms.DateTimeField(),
            #'data_fim' : forms.DateTimeField(),
            #'hora_inicio' : forms.DateTimeField(),
            #'hora_fim' : forms.DateTimeField(),
            'tipo_reserva' : forms.TextInput(attrs={'class': 'form-control'}),
            'pagto' : forms.TextInput(attrs={'class': 'form-control'}),
        }
