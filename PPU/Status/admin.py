from django.contrib import admin
from .models import Sogl, Units, Departure, Act, History

admin.site.register(Units)
admin.site.register(Departure)
admin.site.register(Act)
admin.site.register(History)


class SoglAdmin(admin.ModelAdmin):
    list_display = ('name', 'meropr', 'dogovor', 'value', 'payed',
    'status', 'unit', 'group', 'departure',
    'needs_act',
    )
    list_editable = ('payed', 'status', 'departure', 'needs_act',
    )
    search_fields = ('name',)
    list_filter = ('departure', 'needs_act', 'unit',)
    list_display_links = ('name',)
    empty_value_display = 'Не указано'

admin.site.register(Sogl, SoglAdmin)