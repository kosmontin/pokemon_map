# Generated by Django 3.1.14 on 2022-04-14 18:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20220414_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='evolve_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evolve_to', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционировал'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Имя на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Имя на японском'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 21, 12, 11, 46549), verbose_name='Появится'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]
