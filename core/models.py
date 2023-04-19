from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nome do produto')
    amount = models.IntegerField(verbose_name='Quantidade')
    unitary_value = models.DecimalField(verbose_name='Valor unitário', max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Data de atualização', auto_now=True)


class ProductSold(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    sold_amount = models.IntegerField(verbose_name='Quantidade vendida')
    final_value = models.DecimalField(verbose_name='Valor total', max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)