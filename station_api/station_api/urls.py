import django.contrib.admin
import django.urls


urlpatterns = [
    django.urls.path('', django.urls.include('homepage.urls')),
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('api/v1/', django.urls.include('api_v1.urls')),
]


django.contrib.admin.site.site_header = "QCS API Admin"
django.contrib.admin.site.site_title = "QCS API"
django.contrib.admin.site.index_title = "Welcome to QCS Admin Portal"
