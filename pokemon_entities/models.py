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
    level = models.IntegerField(default=1, verbose_name='Уровень')
    health = models.IntegerField(default=1, verbose_name='Здоровье')
    strength = models.IntegerField(default=1, verbose_name='Атака')
    defence = models.IntegerField(default=1, verbose_name='Защита')
    stamina = models.IntegerField(default=1, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon}, пропадет: {self.disappeared_at}'

    class Meta:
        verbose_name = 'Особь'
        verbose_name_plural = 'Особи'

