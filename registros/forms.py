

from django import forms
from django.forms import ModelForm,Textarea
from registros.models import Ot_Temp_Clima_Interior, Ot_Temp_Minibar, Ot_Pedido_material







class Temp_Clima_Form(forms.ModelForm):
    class Meta:
        model=Ot_Temp_Clima_Interior
        fields= '__all__'
        template_name='ot_registro_edit_form.html'



class Pedido_Form (forms.ModelForm):
    class Meta:
        model=Ot_Pedido_material
        fields= '__all__'
        template_name='ot_Pedidos_edit_form.html'
        widgets={
            'Material':forms.TextInput(attrs={'class':'form-control'} ),
            'estado_ot':forms.Select(attrs={'class':'form-control'}),
         }
