from django.contrib import admin

from .models import Card, Playset, Game

# Register your models here.

admin.site.register(Card)
admin.site.register(Playset)
admin.site.register(Game)