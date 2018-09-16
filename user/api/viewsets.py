from rest_framework import viewsets
from user.models import Profile,Organization,Role
from .serializers import ProfileSerializer,OrgSerializer,RoleSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class  = ProfileSerializer

    __basic_fields = ('user','bio')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

class OrgViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer

    __basic_fields = ('id','name','description')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    __basic_fields = ('id','role','org_id','staff_id')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields
