# # REST API Generic Views
#
# from rest_framework import generics
# from post.models import Post
# from .serializers import PostSerializer
#
# class PostRudView(generics.RetrieveUpdateDestroyAPIView): #Detail View
#     lookup_field        = 'pk'
#     serializer_class    = PostSerializer
#
#     def get_queryset(self):
#         return Post.objects.all()
