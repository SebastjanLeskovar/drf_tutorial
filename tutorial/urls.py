from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
