from models import Ministr, Rozpocet, Vlada
from django.contrib import admin

class MinistrAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('jmeno', )
    }
admin.site.register(Ministr, MinistrAdmin)

class RozpocetAdmin(admin.ModelAdmin):
    list_display = ('rok', 'prijmy', 'vydaje')

admin.site.register(Rozpocet, RozpocetAdmin)

admin.site.register(Vlada)
