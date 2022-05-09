from dataclasses import fields
from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Bo, Natureza, Chave_pix, Conta_corrente, Envolvido

class CadastrarBoForm(ModelForm):
    natureza_crime = ModelMultipleChoiceField(queryset=Natureza.objects.all(), widget=CheckboxSelectMultiple)

    class Meta:
        model = Bo
        fields = ['numero','data_fato','data_registro','local_registro','meios_empregados','natureza_crime','situacao_bo','obs']

class PixForm(ModelForm):

     class Meta:
         model: Chave_pix
         fields = ['pix', 'instituicao']

class ContaForm(ModelForm):

    class Meta:
        model: Conta_corrente
        fields = ['numero', 'agencia', 'instituicao']

class EnvolvidoForm(ModelForm):

    class Meta:
        model = Envolvido
        fields = ['situacao', 'pessoa', 'bo', 'chave_pix', 'conta_corrente', 'telefone_golpe', 'valor_pix', 'valor_cc']