from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from user.models import User,Organization,Role
from .serializers import UserSerializer,OrgSerializer,RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class  = UserSerializer

class OrgViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
