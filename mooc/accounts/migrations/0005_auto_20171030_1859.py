# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171029_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter letras, digitos ou os seguintes caracteres: @/./+/-/_', 'invalid')], unique=True, verbose_name='Nome de Usuário'),
        ),
    ]
