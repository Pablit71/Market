from django.urls import include, path
from rest_framework import routers

from ads.views import AdGetView, AdCreateView, AdUpdateView, AdDeleteView, AdOneGet, CommentViewSet

# TODO настройка роутов для модели

router = routers.SimpleRouter()
router.register('ad/(?P<ad_id>[^/.]+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path("ad/", AdGetView.as_view()),
    path("ad/<int:pk>/", AdOneGet.as_view()),
    path("ad/", AdCreateView.as_view()),
    path("ad/update/<int:pk>", AdUpdateView.as_view()),
    path("ad/delete/<int:pk>", AdDeleteView.as_view()),
]

urlpatterns += router.urls
