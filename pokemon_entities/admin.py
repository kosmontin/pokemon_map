from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Pokemon, PokemonEntity


class PokemonAdmin(admin.ModelAdmin):
    fields = [
        'title', 'title_en', 'title_jp',
        'image', 'preview',
        'description', 'evolve_from'
    ]
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height: 200px;">'
        )

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonEntity)