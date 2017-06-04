from dluhy.models import Ministr, Rozpocet, Vlada, Strana
from django.contrib import admin

class MinistrAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'slug', 'strana')
    prepopulated_fields = {
        'slug': ('jmeno', )
    }
admin.site.register(Ministr, MinistrAdmin)

class StranaAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'slug')
    prepopulated_fields = {
        'slug': ('jmeno', )
    }
admin.site.register(Strana, StranaAdmin)

class RozpocetAdmin(admin.ModelAdmin):
    list_display = ('rok', 'prijmy', 'vydaje')

admin.site.register(Rozpocet, RozpocetAdmin)

admin.site.register(Vlada)
