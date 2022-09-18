from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView

from ads.serializers import AdSerializer

from ads.models import Ad


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class CommentViewSet(viewsets.ModelViewSet):
    pass
