from rest_framework import serializers
from .models import Snippet, Tag


class SnippetSerializer(serializers.ModelSerializer):
    tag = serializers.CharField()

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'tag']

    def create(self, validated_data):
        tag_title = validated_data.pop('tag')
        tag, _ = Tag.objects.get_or_create(title=tag_title)
        return Snippet.objects.create(user=self.context['request'].user, tag=tag, **validated_data)
    

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']
