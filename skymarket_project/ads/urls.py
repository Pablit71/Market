from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

from ads.views import CommentViewSet, AdViewSet

# TODO настройка роутов для модели

ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet)
ads_router.register('ads/(?P<ad_id>[^/.]+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(ads_router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
