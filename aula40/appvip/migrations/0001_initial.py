# Generated by Django 5.1.5 on 2025-01-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('tipo_socio', models.CharField(choices=[('titular', 'Titular')], max_length=10)),
                ('endereco', models.TextField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
