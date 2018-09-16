from rest_framework import routers
from post.api.viewsets import PostViewSet
from user.api.viewsets import ProfileViewSet,OrgViewSet,RoleViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'org', OrgViewSet)
router.register(r'role', RoleViewSet)
