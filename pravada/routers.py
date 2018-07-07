from rest_framework import routers
from post.api.viewsets import PostViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
