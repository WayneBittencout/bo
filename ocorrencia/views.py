import datetime
from inspect import isdatadescriptor
from django.shortcuts import render
from .models import Bo, Chave_pix , Envolvido, Natureza
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CadastrarBoForm
from datetime import date, timedelta
from django.views import generic
from django.urls import reverse_lazy

numero_alerta = 1

def sort_by_valor_total(dados):
  return dados['valor_total']

# Create your views here.
def gtotal():

  valor = {}
  valor['bos'] = Bo.objects.filter(pk__gt=0).count()
  valor['ip'] = Bo.objects.filter(situacao_bo = '5').count()
  valor['tco'] = Bo.objects.filter(situacao_bo = '6').count()
 
    
  return valor


def gpizza():
  naturezas = Natureza.objects.all()
  valores = []
  for natureza in naturezas:
    total = Bo.objects.filter(natureza_crime__id = natureza.id).count()
    valores.append({'name': natureza.descricao, 'y': total})    
  return valores


def gbdelegado(ano):
  
  
  grd = {}
  grd['janeiro']= Bo.objects.filter(situacao_bo = '2', data_registro__month='1' , data_registro__year=ano).count()
  grd['fevereiro']= Bo.objects.filter(situacao_bo = '2', data_registro__month='2' , data_registro__year=ano).count()
  grd['marco']= Bo.objects.filter(situacao_bo = '2', data_registro__month='3' , data_registro__year=ano).count()
  grd['abril']= Bo.objects.filter(situacao_bo = '2', data_registro__month='4' , data_registro__year=ano).count()
  grd['maio']= Bo.objects.filter(situacao_bo = '2', data_registro__month='5' , data_registro__year=ano).count()
  grd['junho']= Bo.objects.filter(situacao_bo = '2', data_registro__month='6' , data_registro__year=ano).count()
  grd['julho']= Bo.objects.filter(situacao_bo = '2', data_registro__month='7' , data_registro__year=ano).count()
  grd['agosto']= Bo.objects.filter(situacao_bo = '2', data_registro__month='8' , data_registro__year=ano).count()
  grd['setembro']= Bo.objects.filter(situacao_bo = '2', data_registro__month='9' , data_registro__year=ano).count()
  grd['outubro']= Bo.objects.filter(situacao_bo = '2', data_registro__month='10' , data_registro__year=ano).count()
  grd['novembro']= Bo.objects.filter(situacao_bo = '2', data_registro__month='11' , data_registro__year=ano).count()
  grd['dezembro']= Bo.objects.filter(situacao_bo = '2', data_registro__month='12' , data_registro__year=ano).count()
  
  return  grd

def gbarquivado(ano):
 
 
  grd = {}
  grd['janeiro']= Bo.objects.filter(situacao_bo = '1', data_registro__month='1' , data_registro__year=ano).count()
  grd['fevereiro']= Bo.objects.filter(situacao_bo = '1', data_registro__month='2' , data_registro__year=ano).count()
  grd['marco']= Bo.objects.filter(situacao_bo = '1', data_registro__month='3' , data_registro__year=ano).count()
  grd['abril']= Bo.objects.filter(situacao_bo = '1', data_registro__month='4' , data_registro__year=ano).count()
  grd['maio']= Bo.objects.filter(situacao_bo = '1', data_registro__month='5' , data_registro__year=ano).count()
  grd['junho']= Bo.objects.filter(situacao_bo = '1', data_registro__month='6' , data_registro__year=ano).count()
  grd['julho']= Bo.objects.filter(situacao_bo = '1', data_registro__month='7' , data_registro__year=ano).count()
  grd['agosto']= Bo.objects.filter(situacao_bo = '1', data_registro__month='8' , data_registro__year=ano).count()
  grd['setembro']= Bo.objects.filter(situacao_bo = '1', data_registro__month='9' , data_registro__year=ano).count()
  grd['outubro']= Bo.objects.filter(situacao_bo = '1', data_registro__month='10' , data_registro__year=ano).count()
  grd['novembro']= Bo.objects.filter(situacao_bo = '1', data_registro__month='11' , data_registro__year=ano).count()
  grd['dezembro']= Bo.objects.filter(situacao_bo = '1', data_registro__month='12' , data_registro__year=ano).count()
  return  grd
  

def gbaoutrasdelegacias(ano):
 
  
  grd = {}
  grd['janeiro']= Bo.objects.filter(situacao_bo = '3', data_registro__month='1' , data_registro__year=ano).count()
  grd['fevereiro']= Bo.objects.filter(situacao_bo = '3', data_registro__month='2' , data_registro__year=ano).count()
  grd['marco']= Bo.objects.filter(situacao_bo = '3', data_registro__month='3' , data_registro__year=ano).count()
  grd['abril']= Bo.objects.filter(situacao_bo = '3', data_registro__month='4' , data_registro__year=ano).count()
  grd['maio']= Bo.objects.filter(situacao_bo = '3', data_registro__month='5' , data_registro__year=ano).count()
  grd['junho']= Bo.objects.filter(situacao_bo = '3', data_registro__month='6' , data_registro__year=ano).count()
  grd['julho']= Bo.objects.filter(situacao_bo = '3', data_registro__month='7' , data_registro__year=ano).count()
  grd['agosto']= Bo.objects.filter(situacao_bo = '3', data_registro__month='8' , data_registro__year=ano).count()
  grd['setembro']= Bo.objects.filter(situacao_bo = '3', data_registro__month='9' , data_registro__year=ano).count()
  grd['outubro']= Bo.objects.filter(situacao_bo = '3', data_registro__month='10' , data_registro__year=ano).count()
  grd['novembro']= Bo.objects.filter(situacao_bo = '3', data_registro__month='11' , data_registro__year=ano).count()
  grd['dezembro']= Bo.objects.filter(situacao_bo = '3', data_registro__month='12' , data_registro__year=ano).count()
  
  return  grd

def grcartorio(ano):
 
  
  grd = {}
  grd['janeiro']= Bo.objects.filter(situacao_bo = '4', data_registro__month='1' , data_registro__year=ano).count()
  grd['fevereiro']= Bo.objects.filter(situacao_bo = '4', data_registro__month='2' , data_registro__year=ano).count()
  grd['marco']= Bo.objects.filter(situacao_bo = '4', data_registro__month='3' , data_registro__year=ano).count()
  grd['abril']= Bo.objects.filter(situacao_bo = '4', data_registro__month='4' , data_registro__year=ano).count()
  grd['maio']= Bo.objects.filter(situacao_bo = '4', data_registro__month='5' , data_registro__year=ano).count()
  grd['junho']= Bo.objects.filter(situacao_bo = '4', data_registro__month='6' , data_registro__year=ano).count()
  grd['julho']= Bo.objects.filter(situacao_bo = '4', data_registro__month='7' , data_registro__year=ano).count()
  grd['agosto']= Bo.objects.filter(situacao_bo = '4', data_registro__month='8' , data_registro__year=ano).count()
  grd['setembro']= Bo.objects.filter(situacao_bo = '4', data_registro__month='9' , data_registro__year=ano).count()
  grd['outubro']= Bo.objects.filter(situacao_bo = '4', data_registro__month='10' , data_registro__year=ano).count()
  grd['novembro']= Bo.objects.filter(situacao_bo = '4', data_registro__month='11' , data_registro__year=ano).count()
  grd['dezembro']= Bo.objects.filter(situacao_bo = '4', data_registro__month='12' , data_registro__year=ano).count()
  
  return  grd

def graficoindex():
  
  grd = {}
  
  grd['100']= Bo.objects.filter(valor_total__gte= '1' , valor_total__lte= '100').count()
  grd['600']= Bo.objects.filter(valor_total__gte= '101' , valor_total__lte= '600').count()
  grd['1200']= Bo.objects.filter(valor_total__gte= '601' , valor_total__lte= '1200').count()
  grd['3000']= Bo.objects.filter(valor_total__gte= '1201' , valor_total__lte= '3000').count()
  grd['5000']= Bo.objects.filter(valor_total__gte= '3001' , valor_total__lte= '5000').count()
  grd['10000']= Bo.objects.filter(valor_total__gte= '5001' , valor_total__lte= '10000').count()
  grd['30000']= Bo.objects.filter(valor_total__gte= '10001' , valor_total__lte= '30000').count()
  grd['50000']= Bo.objects.filter(valor_total__gte= '30001' , valor_total__lte= '50000').count()
  grd['100000']= Bo.objects.filter(valor_total__gte= '50001' , valor_total__lte= '100000').count()
  grd['200000']= Bo.objects.filter(valor_total__gte= '100001' , valor_total__lte= '200000').count()
  grd['300000']= Bo.objects.filter(valor_total__gte= '200001' , valor_total__lte= '300000').count()
  grd['+300000']= Bo.objects.filter(valor_total__gte= '300001').count()

  return  grd




def index(request):
  
  valores = []

  bos = Bo.objects.all().order_by("-valor_total")[:10]
  for bo in bos:
    dados={}
    dados['numero'] = bo.numero
    dados['data'] = bo.data_registro
    dados['valor_total'] = bo.valor_total
    valores.append(dados)
     
  #valores.sort(key=sort_by_valor_total, reverse=True)
   
  return render(request,'ocorrencia/index.html', {"valores":valores, "grafico":graficoindex()})
          
def cadastro(request):
    form = CadastrarBoForm()

    if(request.method == 'POST'):

        form = CadastrarBoForm(request.POST)

        if(form.is_valid()):
            post_numero = form.cleaned_data['numero']
            post_data_fato = form.cleaned_data['data_fato']
            post_data_registro = form.cleaned_data['data_registro']
            post_local_registro = form.cleaned_data['local_registro']
            post_meios_empregados = form.cleaned_data['meios_empregados']
            post_natureza_crime = form.cleaned_data['natureza_crime']
            post_situacao_bo = form.cleaned_data['situacao_bo']
            post_obs = form.cleaned_data['obs']
            print(post_natureza_crime)
            new_post = Bo(numero=post_numero, data_fato=post_data_fato, data_registro=post_data_registro, local_registro=post_local_registro, meios_empregados=post_meios_empregados, situacao_bo=post_situacao_bo, obs=post_obs)
            new_post.save()
            for natureza in post_natureza_crime:
                natureza_obj = Natureza.objects.get(id=natureza.id) #get object by title i.e I declared unique for title under Category model
                new_post.natureza_crime.add(natureza_obj)
            #messages.error(request, 'As senhas devem ser iguais')
            return redirect('index')

    elif(request.method == 'GET'):
        return render(request,'ocorrencia/cadastro.html', {'form': form})

class BoAtualizar(generic.UpdateView):
  model = Bo
  form_class = CadastrarBoForm
  template_name = 'ocorrencia/bo_editar.html'
  success_url = reverse_lazy('lista-bo')
  success_message = "Fonte Atualizada"

class BoLista(generic.ListView):
  model = Bo
  context_object_name = 'lista_bos'
  template_name = 'ocorrencia/bo_lista.html'
  paginate_by = 10


def graficos(request, ano=date.today().year):
   
  valor={}
  if request.GET.get('ano'):
    ano = request.GET.get('ano')
  valor['delegado'] =  gbdelegado(ano)
  valor['arquivado'] =  gbarquivado(ano)
  valor['outrasdelegacias'] =  gbaoutrasdelegacias(ano)
  valor['cartorio'] =  grcartorio(ano)
  valor['dados'] = gpizza()
  valor['total'] = gtotal()
  

  return render(request,'ocorrencia/graficos.html', valor)

def validadata(ndata):

  current_date = date.today()
  datainsercao = ndata
  valida = current_date - timedelta(5)
  
  if datainsercao >= valida:
    return TRUE

def alertas_fone():

  lista = []
  telefone_golpe_dias = set()
  envolvidos_ultimos_bos = Envolvido.objects.filter(bo__data_insercao__range = [datetime.date.today() - datetime.timedelta(days=5), datetime.date.today()])
  for envolvido in envolvidos_ultimos_bos:
    #print(envolvido.bo.numero)
    if envolvido.telefone_golpe:
       telefone_golpe_dias.add(envolvido.telefone_golpe)
  
  for fone in telefone_golpe_dias:
    envolvidos = Envolvido.objects.filter(telefone_golpe = fone)
    lista_bos = []
    for envolvido in envolvidos:
      lista_bos.append(envolvido.bo.numero)
    if len(lista_bos) > numero_alerta:
     lista.append({'telefone': fone, 'bos': lista_bos})

  #print(lista)
  #print(telefone_golpe_dias)
    
  

  return lista





def alertas_cc():

  lista = []
  conta_corrente_dias = set()
  envolvidos_ultimos_bos = Envolvido.objects.filter(bo__data_insercao__range = [datetime.date.today() - datetime.timedelta(days=5), datetime.date.today()])
  for envolvido in envolvidos_ultimos_bos:
    #print(envolvido.bo.numero)
    if envolvido.conta_corrente is not None:
      conta_corrente_dias.add(envolvido.conta_corrente.numero)
  
  for cc in conta_corrente_dias:
    envolvidos = Envolvido.objects.filter(conta_corrente__numero = cc)
    lista_bos = []
    for envolvido in envolvidos:
      lista_bos.append(envolvido.bo.numero)
    if len(lista_bos) > numero_alerta:
      lista.append({'conta': cc, 'bos': lista_bos})

  #print(lista)
  #print(conta_corrente_dias)
    
  

  return lista



def alertas(request):

  lista = []
  chaves_pix_ultimos_dias = set()
  envolvidos_ultimos_bos = Envolvido.objects.filter(bo__data_insercao__range = [datetime.date.today() - datetime.timedelta(days=5), datetime.date.today()])
  for envolvido in envolvidos_ultimos_bos:
   # print(envolvido.bo.numero)
    if envolvido.chave_pix is not None:
      chaves_pix_ultimos_dias.add(envolvido.chave_pix.pix)
  
  for chave in chaves_pix_ultimos_dias:
    envolvidos = Envolvido.objects.filter(chave_pix__pix = chave)
    lista_bos = []
    for envolvido in envolvidos:
      lista_bos.append(envolvido.bo.numero)
    if len(lista_bos) > numero_alerta:
      lista.append({'pix': chave, 'bos': lista_bos})

 # print(lista)
 # print(chaves_pix_ultimos_dias)
    
  

  return render(request,'ocorrencia/alerta.html', {"alerta":lista, "alertacc":alertas_cc(), "alertafone":alertas_fone()})

