from django.contrib import admin

from .models import Post, BaseComment, Reply, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(BaseComment)
admin.site.register(Reply)
admin.site.register(Category)
