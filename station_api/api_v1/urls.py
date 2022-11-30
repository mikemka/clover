import django.urls
import api_v1.views


urlpatterns = [
    django.urls.path('ping/', api_v1.views.ping),
    django.urls.path('get_station/', api_v1.views.get_station),
]
