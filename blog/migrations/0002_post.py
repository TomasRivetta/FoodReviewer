# Generated by Django 4.1 on 2022-09-16 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=80, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=120, verbose_name='Descripcion')),
                ('contenido', models.CharField(max_length=1200)),
                ('imagen', models.ImageField(max_length=255, upload_to='')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de  creacion')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
