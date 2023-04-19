# Generated by Django 4.2 on 2023-04-18 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nome do produto')),
                ('amount', models.IntegerField(verbose_name='Quantidade')),
                ('unitary_value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor unitário')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_amount', models.IntegerField(verbose_name='Quantidade vendida')),
                ('final_value', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor total')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.product')),
            ],
        ),
    ]
