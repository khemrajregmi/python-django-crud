from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import ItemViewSet, UserViewSet, home

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),  # Add this line to handle the root URL
]
