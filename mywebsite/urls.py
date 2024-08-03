from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), # This means after the url not starting in 'admin/' goes here. To myapp.urls
]
