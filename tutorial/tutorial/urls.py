from django.conf.urls import include, url
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url('', include('snippets.urls')),
    url('schema/', schema_view),
]
