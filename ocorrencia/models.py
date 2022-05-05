from datetime import date
from django.db import models
from django.dispatch import receiver 
from django.utils import timezone

# Create your models here.
#blank siguifica opcional, adiciona impot timezone pra data automatica,def str pra mudar o nome ficar certo na categoria

class Natureza(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class Bo(models.Model):
    ESCOLHA =(
        (u'1', u'Arquivado'),
        (u'2', u'Delegado'),
        (u'3', u'Outras Delegacias'),
        (u'4', u'Aguardando em Cartorio'),
        (u'5', u'Instaurados IP'),
        (u'6', u'Instaurados TCO'),
    )
    
    numero = models.CharField(max_length=255, unique=True)
    data_fato = models.DateField()
    data_registro = models.DateField()
    local_registro = models.CharField(max_length=255)
    meios_empregados = models.CharField(max_length=255)
    natureza_crime = models.ManyToManyField(Natureza, related_name='naturezas')
    situacao_bo = models.CharField(max_length=1, choices=ESCOLHA)
    obs = models.TextField()
    data_insercao= models.DateField(default=date.today)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True,default=0)   

    def __str__(self):
        return self.numero

       
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=255, blank=True, unique=True )
    rg = models.CharField(max_length=255, blank=True, unique=True)
    telefone = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"{self.nome} - {self.cpf_cnpj}"
    

class Conta_corrente(models.Model):
    numero = models.CharField(max_length=255, blank=True)
    agencia = models.CharField(max_length=255, blank=True)
    instituicao = models.CharField(max_length=255, blank=True)
   
    def __str__(self):
     return f'{self.numero}'
    

class Chave_pix(models.Model):
    pix = models.CharField(max_length=255, blank=True, unique=True)
    instituicao = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
     return f'{self.pix}'


class Envolvido(models.Model):
    ESCOLHA =(
        (u'1', u'Infrator'),
        (u'2', u'Vítima'),
    )
    situacao = models.CharField(max_length=1, choices=ESCOLHA)
    pessoa = models.ForeignKey(Pessoa, on_delete= models.CASCADE, related_name='pessoas')
    bo = models.ForeignKey(Bo, on_delete= models.CASCADE, related_name='bos')
    chave_pix = models.ForeignKey(Chave_pix, on_delete= models.CASCADE, blank=True,null=True, related_name="pixs")
    conta_corrente= models.ForeignKey(Conta_corrente, on_delete= models.CASCADE, blank=True,null=True ,related_name="cc")
    telefone_golpe = models.CharField(max_length=255, blank=True)
    valor_pix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    valor_cc = models.DecimalField(max_digits=10, decimal_places=2, blank=True,default=0)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True,default=0)

    def save(self, *args,**kwargs):
        self.valor_total = self.valor_cc + self.valor_pix
        return super().save(*args,**kwargs)

    def __str__(self):
     return f'{self.pessoa.nome}'


@receiver(models.signals.post_save, sender=Envolvido)
def atualizar_bo(sender, instance, **kwargs):
    valortotal = 0
    envolvidos = instance.bo.bos.all()
    for envolvido in envolvidos:
        valortotal = valortotal + envolvido.valor_total
    instance.bo.valor_total = valortotal
    instance.bo.save()