# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20171024_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joianed',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(verbose_name='Data de Entrada', default=0, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter letras, digitos ou os seguintes caracteres: @/./+/-/_', 'invalid')], max_length=30, verbose_name='Nome de Usuário'),
        ),
    ]
