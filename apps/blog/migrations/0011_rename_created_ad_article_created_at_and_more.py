# Generated by Django 4.0.6 on 2022-08-04 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='created_ad',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='updatet_at',
            new_name='updated_at',
        ),
    ]
