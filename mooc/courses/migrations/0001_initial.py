# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descrição Simples')),
                ('about', models.TextField(blank=True, verbose_name='Sobre o Curso')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de Início')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Cursos',
                'verbose_name': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, default=0, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], verbose_name='Situação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(to='courses.Course', related_name='enrollments', verbose_name='Curso')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='enrollments', verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Inscrições',
                'verbose_name': 'Inscrição',
            },
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('user', 'course')]),
        ),
    ]
