from django.contrib import admin
from .models import State, LGA

# Register your models here.
@admin.register(LGA)
class LgaAdmin(admin.ModelAdmin):
    # Main LGA adminssss
    list_display = (
        'state',
        'name',
        'longitude',
        'latitude',
        'population',
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
        'longitude',
        'latitude',
        'population'
    )

    list_editable = (
        'capital',
        'longitude',
        'latitude',
        'population',
    )

    list_filter = ('state',)

    fields = [
        ('state', 'capital'),
        ('longitude', 'latitude'),
        'population',
    ]

    search_fields = ['state']
    inlines = [LgaInstance]
