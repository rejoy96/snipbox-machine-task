from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse


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


class SnippetDeleteView(generics.DestroyAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        snippets = Snippet.objects.filter(user=request.user)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagDetailView(generics.ListAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tag_id = self.kwargs['pk']
        return Snippet.objects.filter(user=self.request.user, tag_id=tag_id)
    

class SnippetOverviewView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        snippets = Snippet.objects.filter(user=request.user)
        total = snippets.count()
        data = {
            'total_snippets': total,
            'snippets': [
                {
                    'id': snippet.id,
                    'title': snippet.title,
                    'detail_url': request.build_absolute_uri(
                        reverse('snippet-detail', args=[snippet.id])
                    )
                }
                for snippet in snippets
            ]
        }
        return Response(data)
