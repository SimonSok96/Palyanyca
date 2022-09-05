from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill

from config.settings import MEDIA_ROOT


class User(AbstractUser):
    phone = models.CharField(verbose_name='Телефон', max_length=13, null=True, blank=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='user/',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 100}
    )
    about = models.TextField(verbose_name='О себе', blank=True, null=True)

    def image_teg_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                User.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='70'>")

    image_teg_thumbnail.short_description = 'Текущее изображение'
    image_teg_thumbnail.allow_tags = True


    def image_teg(self):
        if self.image:
            if not self.image_thumbnail:
                User.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}'>")

    image_teg.short_description = 'Текущее изображение'
    image_teg.allow_tags = True

