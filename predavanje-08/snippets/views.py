from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SnippetSerializer
from .models import Snippet


class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Snippet.objects.all().order_by('-title')
    serializer_class = SnippetSerializer
    # permission_classes = [permissions.IsAuthenticated]
