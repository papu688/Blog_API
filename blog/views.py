from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer

class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
