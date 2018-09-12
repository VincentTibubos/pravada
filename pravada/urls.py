from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
# from .routers import router

urlpatterns = [
    path('',include('app.urls')),
    path('admin/', admin.site.urls)
    # path('api/', include(router.urls))
]
