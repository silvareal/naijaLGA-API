

from django.contrib import admin
from .models import State, LGA, Coord

# Register your models here
class CoordInstance(admin.TabularInline):
    # Inline LGA Cord(lat, long)
    model = Coord


@admin.register(LGA)
class LgaAdmin(admin.ModelAdmin):
    # Main LGA adminssss
    list_display = (
        'state',
        'name',
        'population',
        'coord',
    )
    search_fields = ['state']
    list_filter = ('state',)


class LgaInstance(admin.TabularInline):
    # Inline lga instance
    model = LGA


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    # Main state adminss
    list_display = (
        'state',
        'capital',
        'population'
    )

    list_editable = (
        'capital',
        'population',
    )

    list_filter = ('state',)

    fields = [
        ('state', 'capital'),
        'population',
        'coord',
    ]

    search_fields = ['state']
    inlines = [LgaInstance]

admin.site.register(Coord)