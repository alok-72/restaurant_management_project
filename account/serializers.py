from rest_frameworks import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'created_at']
        read_only_fields = ['created_at']