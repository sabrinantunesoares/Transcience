# Generated by Django 5.1.1 on 2024-09-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='foto',
            field=models.ImageField(default='biblioteca/images/perfil/foto_perfil.png', upload_to='biblioteca/images/perfil/'),
        ),
    ]
