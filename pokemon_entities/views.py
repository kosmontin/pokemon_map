import datetime
import json

import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemon_entities = PokemonEntity.objects.filter(
        disappeared_at__gte=datetime.datetime.now()
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in pokemon_entities:
        add_pokemon(
            folium_map,
            entity.lat,
            entity.lon,
            request.build_absolute_uri(
                entity.pokemon.image.url
            ) if entity.pokemon.image else DEFAULT_IMAGE_URL
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.pk,
            'img_url':
                pokemon.image.url if pokemon.image else DEFAULT_IMAGE_URL,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk=pokemon_id)
    evolve_from_pokemon = Pokemon.objects.filter(
        pk=pokemon.evolve_from_id).first()
    evolve_to_pokemon = pokemon.evolve_to.all().first()
    serialized_pokemon = {
        'pokemon_id': pokemon.pk,
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'img_url': pokemon.image.url,
        'description': pokemon.description,
    }
    if evolve_from_pokemon:
        serialized_pokemon['previous_evolution'] = {
            'pokemon_id': evolve_from_pokemon.pk,
            'title_ru': evolve_from_pokemon.title,
            'img_url': evolve_from_pokemon.image.url
        }
    if evolve_to_pokemon:
        serialized_pokemon['next_evolution'] = {
            'pokemon_id': evolve_to_pokemon.pk,
            'title_ru': evolve_to_pokemon.title,
            'img_url': evolve_to_pokemon.image.url
        }
    pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.image.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': serialized_pokemon
    })
