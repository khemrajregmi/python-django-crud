# myapp/views.py
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def home(request):
    return HttpResponse("<h1>Welcome to the API this </h1><p>Navigate to <a href='/api/items/'>/api/items/</a> to use the API.</p>")
