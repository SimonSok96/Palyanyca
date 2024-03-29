# Generated by Django 4.0.6 on 2022-08-15 13:26

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата сездания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/category', verbose_name='Изображение'),
        ),
    ]
