from django.forms import ModelForm
from .models import Bo
class PostForm(ModelForm):
    class Meta:
        model = Bo
        fields = ['numero','data_fato','data_registro','local_registro','meios_empregados','natureza_crime','situacao_bo','obs']