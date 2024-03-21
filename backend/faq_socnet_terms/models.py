from django.db import models


class FAQ(models.Model):
    question = models.CharField(verbose_name='Питання', max_length=200)

    answer = models.CharField(verbose_name='Відповідь', max_length=200)

    is_published = models.BooleanField(verbose_name='Показувати на сайті?', default=True)


    class Meta:
        verbose_name = 'Поширене запитання'
        verbose_name_plural = 'Поширені запятання'

    def __str__(self):
        return self.question


class SocialNetworks(models.Model):
    title = models.CharField(verbose_name='Соціальна мережа', max_length=200)

    link = models.CharField(verbose_name='Посилання', max_length=200)

    is_published = models.BooleanField(verbose_name='Показувати на сайті?', default=True)


    class Meta:
        verbose_name = 'Соціальна мережа'
        verbose_name_plural = 'Соціальні мережі'

    def __str__(self):
        return self.title


class Terms(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)

    text = models.CharField(verbose_name='Текст', max_length=200)

    is_published = models.BooleanField(verbose_name='Показувати на сайті?', default=True)


    class Meta:
        verbose_name = 'Умова користування'
        verbose_name_plural = 'Умови користування'

    def __str__(self):
        return self.title