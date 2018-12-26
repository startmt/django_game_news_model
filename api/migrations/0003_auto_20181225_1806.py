# Generated by Django 2.1.4 on 2018-12-25 11:06

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default='', verbose_name='Content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='image_header',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
