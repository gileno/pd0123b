# Generated by Django 4.2.1 on 2023-06-20 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_inscricao_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data criação')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Data modificação')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
            },
        ),
        migrations.AlterModelOptions(
            name='inscricao',
            options={'ordering': ['-data'], 'verbose_name': 'Inscrição', 'verbose_name_plural': 'Inscrições'},
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Data do Evento')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data criação')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Data modificação')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'ordering': ['-criado_em'],
            },
        ),
    ]
