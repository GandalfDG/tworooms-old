from django.contrib import admin

from .models import Card, Playset, Game, Player

# Register your models here.

admin.site.register(Card)
admin.site.register(Playset)
admin.site.register(Game)
admin.site.register(Player)