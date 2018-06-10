from django.urls import path, re_path
from .views import PostRudView

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', PostRudView.as_view(), name='post-rud')
]
 
