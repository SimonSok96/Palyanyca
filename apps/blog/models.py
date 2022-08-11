from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill

from apps.user.models import User
from config.settings import MEDIA_ROOT


class BlogCategory(models.Model):
    name = models.CharField(verbose_name= 'Название', max_length= 255)
    # image = models.ImageField(verbose_name='Зображення', upload_to='blog/category/', null=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
        null=True
    )

    def image_teg_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_teg_thumbnail.short_description = 'Текущее изображение'
    image_teg_thumbnail.allow_tags = True


    def image_teg(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_teg.short_description = 'Текущее изображение'
    image_teg.allow_tags = True


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории блогов'


class Teg(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):
    category = models.ForeignKey(
        to= BlogCategory,
        verbose_name= 'Категория',
        on_delete= models.SET_NULL,
        null= True,
    )
    user = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True
    )
    tegs = models.ManyToManyField(to=Teg, verbose_name='Теги')
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/article/',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100}
    )
    title = models.CharField(verbose_name= 'Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name= 'Текст-превью')
    text = models.TextField(verbose_name= 'Текст')
    created_at = models.DateTimeField(verbose_name= 'Дата создания', auto_now_add= True)
    updated_at = models.DateTimeField(verbose_name= 'Дата редактирования', auto_now_add= True)


    def image_teg_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                Article.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='70'>")

    image_teg_thumbnail.short_description = 'Текущее изображение'
    image_teg_thumbnail.allow_tags = True


    def image_teg(self):
        if self.image:
            if not self.image_thumbnail:
                Article.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}'>")

    image_teg.short_description = 'Текущее изображение'
    image_teg.allow_tags = True


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Cтатьи'