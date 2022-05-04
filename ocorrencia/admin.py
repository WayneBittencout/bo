#from re import search
from django.contrib import admin
from .models import Bo , Pessoa ,Envolvido,Conta_corrente,Chave_pix, Natureza

class EnvolvidosInline(admin.TabularInline):
    model = Envolvido
    extra = 0
    autocomplete_fields= ('pessoa','chave_pix','conta_corrente')

class BoAdmin(admin.ModelAdmin):
  list_display = ('id','numero', 'data_fato','data_registro','situacao_bo')
  list_display_links = ('id','numero')
 # list_filter= ('nome','sobrenome')
  readonly_fields = ["data_insercao", "valor_total"] #bloqueia insercao
  list_per_page = 10
  search_fields = ('numero','data_fato')
  inlines = (EnvolvidosInline,)
  filter_horizontal = ('natureza_crime',)

class PessoaAdmin(admin.ModelAdmin):
  list_display = ('nome','cpf_cnpj', 'rg','telefone',)
 # list_display_links = ('id','cpf_cnpj')
  #list_filter= ('conta','pix')
  list_per_page = 10
  search_fields = ('nome','cpf_cnpj', 'rg' , 'pessoas__telefone_golpe')
  inlines = (EnvolvidosInline,)

class Chave_pixAdmin(admin.ModelAdmin):
  list_display = ('pix','instituicao')
  list_display_links = ('pix',)
  list_per_page = 10
  search_fields = ('pix',)
  inlines = (EnvolvidosInline,)
  

class Conta_correnteAdmin(admin.ModelAdmin):
  list_display = ('numero','agencia', 'instituicao')
  list_display_links = ('numero','agencia','instituicao')
  list_per_page = 10
  search_fields = ('numero', 'agencia')
  inlines = (EnvolvidosInline,)
  

admin.site.register(Natureza) 
admin.site.register(Bo, BoAdmin)
admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Chave_pix, Chave_pixAdmin)
admin.site.register(Conta_corrente, Conta_correnteAdmin)
