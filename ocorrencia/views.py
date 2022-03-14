from datetime import datetime
from itertools import count
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bo
from datetime import date


# Create your views here.
def gtotal():

  valor = {}
  valor['bos'] = Bo.objects.filter(pk__gt=0).count()
  valor['arquivado'] = Bo.objects.filter(situacao_bo = '1').count()
  valor['outrasdelegacias'] = Bo.objects.filter(situacao_bo = '3').count()
 
    
  return valor


def gpizza():

  valor = {}
  valor['estelinato'] = Bo.objects.filter(natureza_crime = '1').count()
  valor['tentativaestelinato'] = Bo.objects.filter(natureza_crime = '2').count()
  valor['furto'] = Bo.objects.filter(natureza_crime = '3').count()
  valor['invasaodedispositivo']= Bo.objects.filter(natureza_crime = '4').count()
  valor['ameaca'] = Bo.objects.filter(natureza_crime = '5').count()
  valor['outrosfatos'] = Bo.objects.filter(natureza_crime = '6').count()
  dados = []
  dados.append({'name': 'Estelionato', 'y': valor['estelinato']})
  dados.append({'name': 'Tentativa de Estelionato', 'y': valor['tentativaestelinato']})
  dados.append({'name': 'Furto', 'y': valor['furto']})
  dados.append({'name': 'Invasao de Dispositivo', 'y': valor['invasaodedispositivo']})
  dados.append({'name': 'Ameaca', 'y': valor['ameaca']})
  dados.append({'name': 'Outros Fatos', 'y': valor['outrosfatos']})
    
  return dados


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


def index(request, ano=date.today().year):
   
  valor={}
  if request.GET.get('ano'):
    ano = request.GET.get('ano')
  valor['delegado'] =  gbdelegado(ano)
  valor['arquivado'] =  gbarquivado(ano)
  valor['outrasdelegacias'] =  gbaoutrasdelegacias(ano)
  valor['dados'] = gpizza()
  valor['total'] = gtotal()
  

  return render(request,'ocorrencia/index.html', valor)

