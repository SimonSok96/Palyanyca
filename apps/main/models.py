from django.db import models
from tinymce.models import HTMLField

from apps.main.mixins import MetaTegMixin


class Page(MetaTegMixin):
    name = models.CharField(verbose_name='Название', max_length=120)
    slug = models.SlugField(unique=True)
    text = HTMLField(verbose_name='Описание', null=True)
    is_active = models.BooleanField(verbose_name='Активироывно', default=True)

    class Meta:
        verbose_name = 'Информационная страница'
        verbose_name_plural = 'Информационные страницы'

    def __str__(self):
        return self.name
