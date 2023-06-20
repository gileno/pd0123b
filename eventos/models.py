from django.db import models


class Inscricao(models.Model):

    INTERESSE_OPCOES = (
        ('show', 'Shows de Música'),
        ('futebol', 'Jogos de Futebol'),
        ('outros', 'Outros'),
    )

    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='E-mail')
    interesse = models.CharField(verbose_name='Interesse', max_length=50, choices=INTERESSE_OPCOES)
    observacoes = models.TextField(verbose_name='Observações', blank=True)
    data = models.DateTimeField(verbose_name='Data criação', auto_now_add=True, null=True)

    # class Meta:
    #     db_table = 'inscricao'
