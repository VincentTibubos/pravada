from rest_framework import routers
from user.api.viewsets import UserViewSet,OrgViewSet,RoleViewSet
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'org', OrgViewSet)
router.register(r'role', RoleViewSet)
