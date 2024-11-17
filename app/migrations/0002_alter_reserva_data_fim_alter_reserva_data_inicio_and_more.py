# Generated by Django 5.1.3 on 2024-11-16 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_fim',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='data_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='email_cliente',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_fim',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_inicio',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='nome_cliente',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='pagto',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='rg_cliente',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='tipo_reserva',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
