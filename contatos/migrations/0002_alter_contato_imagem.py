# Generated by Django 4.2 on 2023-04-25 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]