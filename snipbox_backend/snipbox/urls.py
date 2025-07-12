
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SnippetCreateView, SnippetDetailView, SnippetUpdateView, SnippetDeleteView, \
    TagListView, TagDetailView, SnippetOverviewView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('snippets/create/', SnippetCreateView.as_view(), name='snippet-create'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/update/',
         SnippetUpdateView.as_view(), name='snippet-update'),
    path('snippets/<int:pk>/delete/',
         SnippetDeleteView.as_view(), name='snippet-delete'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('snippets/', SnippetOverviewView.as_view(), name='snippet-overview'),


    
]
