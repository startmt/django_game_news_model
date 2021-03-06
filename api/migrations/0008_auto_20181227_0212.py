# Generated by Django 2.1.4 on 2018-12-26 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20181227_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_comment',
            new_name='comment_user_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_article_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='api.Article'),
            preserve_default=False,
        ),
    ]
