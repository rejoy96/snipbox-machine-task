from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Snippet
from .serializers import SnippetSerializer


class SnippetCreateView(generics.CreateAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]
