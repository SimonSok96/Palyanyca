from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from apps.api.blog.serializers import ArticleReadSerializer, ArticleWriteSerializer
from apps.blog.models import Article, Teg


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ArticleReadSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ArticleWriteSerializer
        return self.serializer_class

    @staticmethod
    def chack_tags(tags):
        tegs_list = []
        for item in tags:
            teg = Teg.objects.filter(name=item).first()
            if not teg:
                teg = Teg.objects.create(name=item)
            tegs_list.append(teg)
        return tegs_list

    def save_model(self, serializer):
        serializer.is_valid(raise_exception=True)
        tegs = serializer.validated_data.get('tegs')
        article = serializer.save(user=self.request.user, tegs=self.chack_tags(tegs))
        read_serializer = self.serializer_class(article, context={'request': self.request})
        return read_serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        read_serializer = self.save_model(serializer)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        read_serializer = self.save_model(serializer)
        return Response(read_serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Article.objects.all()
        if self.request.query_params.get('user'):
            queryset = queryset.filter(user=self.request.query_params.get('user'))
        if self.request.query_params.get('category'):
            queryset = queryset.filter(category=self.request.query_params.get('category'))

        return queryset
