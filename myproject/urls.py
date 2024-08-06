from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import ItemViewSet, home  # Import home from myapp.views

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),  # Add this line to handle the root URL
]
