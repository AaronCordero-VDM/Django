# Generated by Django 5.0.1 on 2024-01-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Foto del artículo'),
        ),
    ]