from django.conf.urls import include, url
from django.urls import path

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    path('schema/', schema_view),
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
