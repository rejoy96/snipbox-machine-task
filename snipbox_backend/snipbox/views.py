from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Snippet
from .serializers import SnippetSerializer


class SnippetCreateView(generics.CreateAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]


class SnippetDetailView(generics.RetrieveAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)
