# Generated by Django 4.1 on 2022-09-16 23:03

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_posteo_delete_posteos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]