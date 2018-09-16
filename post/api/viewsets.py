from rest_framework import viewsets
from post.models import Post
from post.api.serializers import PostSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    fields = ('title', 'text')

    __basic_fields = ('title',)
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields
