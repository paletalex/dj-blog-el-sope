# Generated by Django 2.2 on 2019-12-28 20:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Paginas',
                'ordering': ['title'],
            },
        ),
    ]
