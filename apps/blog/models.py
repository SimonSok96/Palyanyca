from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(verbose_name= 'Название', max_length= 255)

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
    tegs = models.ManyToManyField(to=Teg, verbose_name='Теги')
    title = models.CharField(verbose_name= 'Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name= 'Текст-превью')
    text = models.TextField(verbose_name= 'Текст')
    created_ad = models.DateTimeField(verbose_name= 'Дата создания', auto_now_add= True)
    updatet_at = models.DateTimeField(verbose_name= 'Дата редактирования', auto_now_add= True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Cтатьи'