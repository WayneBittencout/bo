from django.db import models 
from django.utils import timezone

# Create your models here.
#blank siguifica opcional, adiciona impot timezone pra data automatica,def str pra mudar o nome ficar certo na categoria


class Bo(models.Model):
    ESCOLHA =(
        (u'1', u'Arquivado'),
        (u'2', u'Delegado'),
        (u'3', u'Outras Delegacias'),
    )
    NATUREZA =(
        (u'1', u'ESTELIONATO'),
        (u'2', u'TENTATIVA DE ESTELIONATO'),
        (u'3', u'FURTO'),
        (u'4', u'INVASAO DE DISPOSITIVO'),
        (u'5', u'AMEAÇA'),
        (u'6', u'OUTROS FATOS ATIPICOS'),
    )
    numero = models.CharField(max_length=255)
    data_fato = models.DateField()
    data_registro = models.DateField()
    local_registro = models.CharField(max_length=255)
    meios_empregados = models.CharField(max_length=255)
    natureza_crime = models.CharField(max_length=1, choices=NATUREZA)
    situacao_bo = models.CharField(max_length=1, choices=ESCOLHA)
    obs = models.TextField()
    def __str__(self):
        return self.numero

       
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=255, blank=True)
    rg = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.nome
    

class Conta_corrente(models.Model):
    numero = models.CharField(max_length=255)
    agencia = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=255)

    def __str__(self):
     return f'{self.numero}'
    

class Chave_pix(models.Model):
    pix = models.CharField(max_length=255)

    def __str__(self):
     return f'{self.pix}'


class Envolvido(models.Model):
    ESCOLHA =(
        (u'1', u'Infrator'),
        (u'2', u'Vítima'),
    )
    situacao = models.CharField(max_length=1, choices=ESCOLHA)
    pessoa = models.ForeignKey(Pessoa, on_delete= models.CASCADE)
    bo = models.ForeignKey(Bo, on_delete= models.CASCADE)
    chave_pix = models.ForeignKey(Chave_pix, on_delete= models.CASCADE)
    conta_corrente= models.ForeignKey(Conta_corrente, on_delete= models.CASCADE)

    def __str__(self):
     return f'{self.pessoa.nome}'

