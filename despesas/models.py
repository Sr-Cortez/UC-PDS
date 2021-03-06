from django.db import models
from django.db.models.deletion import CASCADE
from contas.models import Contas


class Despesas(models.Model):
    """
    Modelo para a tabela Despesas

    Args:
        models (Model): Contém todos os campos essenciais e comportamentos dos dados armazenados
    """

    opcoes_tipo_despesa = [
        ('', '--------'),
        ('AL', 'Alimentação'),
        ('ED', 'Educação'),
        ('LA', 'Lazer'),
        ('MO', 'Moradia'),
        ('RO', 'Roupa'),
        ('SA', 'Saúde'),
        ('TR', 'Transporte'),
        ('OU', 'Outros')
    ]

    valor = models.DecimalField(max_digits=15, decimal_places=2)
    dataPagamento = models.DateField(verbose_name='Data pagamento')
    dataPagamentoEsperado = models.DateField(
        verbose_name='Data pagamento esperado', null=True, blank=True)
    conta = models.ForeignKey(Contas, on_delete=CASCADE)
    tipoDespesa = models.CharField(
        max_length=2, choices=opcoes_tipo_despesa, verbose_name='Tipo')

    def __str__(self) -> str:
        return f'{self.get_tipoDespesa_display()} - R$ {self.valor}'
