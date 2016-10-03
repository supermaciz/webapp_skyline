from django.conf.urls import url
from connection.views import hello

urlpatterns = [
    url(r'^/?', hello),
]
