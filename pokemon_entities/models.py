import datetime

from django.db import models  # noqa F401


class Pokemon(models.Model):
    '''Покемон'''
    title = models.CharField(max_length=200, verbose_name='Имя')
    image = models.ImageField(blank=True, null=True, verbose_name='Картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'


class PokemonEntity(models.Model):
    '''Особь'''
    pokemon = models.ForeignKey(Pokemon, default=None, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Появится')
    disappeared_at = models.DateTimeField(default=None, verbose_name='Пропадет')


