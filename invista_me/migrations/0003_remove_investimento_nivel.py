# Generated by Django 4.1.7 on 2023-06-29 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0002_investimento_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimento',
            name='nivel',
        ),
    ]