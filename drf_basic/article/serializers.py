from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=100)
    # content = serializers.CharField()
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "created_at"]
        read_only_fields = ["id", "created_at"]

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=100)
    # created_at = serializers.DateTimeField(read_only=True)
