from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Snippet, Tag
from .serializers import SnippetSerializer


class SnippetCreateView(generics.CreateAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]


class SnippetDetailView(generics.RetrieveAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)


class SnippetUpdateView(generics.UpdateAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        tag_title = self.request.data.get("tag")
        if tag_title:
            tag, _ = Tag.objects.get_or_create(title=tag_title)
            serializer.save(tag=tag)
        else:
            serializer.save()
