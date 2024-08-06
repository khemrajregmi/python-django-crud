from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer, UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
    return HttpResponse("<h1>Welcome to the API</h1><p>Navigate to <a href='/api/items/'>/api/items/</a> to use the API.</p>")
