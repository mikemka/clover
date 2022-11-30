import django.contrib.admin
import api_v1.models


@django.contrib.admin.register(api_v1.models.Station)
class StationAdmin(django.contrib.admin.ModelAdmin):
    list_display = ('name', 'aruco_marker', 'status', 'show_token')
    list_filter = ('status', 'charging')
