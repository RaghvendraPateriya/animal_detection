from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('upload', views.AnimalImage, basename="animal")
router.register('client', views.ClientViewSet, basename="client")

urlpatterns = [
    path('api/', include(router.urls)),
]
