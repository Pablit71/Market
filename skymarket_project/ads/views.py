from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from ads.serializers import AdSerializer, AdOneSerializer, AdDeleteSerializer, CommentSerializer,\
    CommentListSerializer, \
    CommentCreateSerializer

from ads.models import Ad, Comment


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdGetView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdOneGet(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdOneSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDeleteSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    serializer_action_classes = {
        'list': CommentListSerializer,
        'create': CommentCreateSerializer,
    }

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_id'])

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs['ad_id'])
        serializer.save(author=self.request.user, ad=ad)
