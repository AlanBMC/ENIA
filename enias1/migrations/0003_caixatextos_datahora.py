# Generated by Django 5.0.1 on 2024-02-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enias1', '0002_remove_usuario_pagina_pagina_usuario_usuario_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='caixatextos',
            name='datahora',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
