from django.db import models  # noqa F401


class Pokemon(models.Model):
    '''Покемон'''
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

