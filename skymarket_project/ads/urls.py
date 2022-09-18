from django.urls import include, path

from ads.views import AdViewSet

# TODO настройка роутов для модели


urlpatterns = [
    path("ad/", AdViewSet.as_view())
]
