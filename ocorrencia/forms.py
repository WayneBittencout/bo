from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Bo, Natureza

class PostForm(ModelForm):
    natureza_crime = ModelMultipleChoiceField(queryset=Natureza.objects.all(), widget=CheckboxSelectMultiple)

    class Meta:
        model = Bo
        fields = ['numero','data_fato','data_registro','local_registro','meios_empregados','natureza_crime','situacao_bo','obs']