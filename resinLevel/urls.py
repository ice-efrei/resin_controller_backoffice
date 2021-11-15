from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'resin', views.ResinViewSet)
router.register(r'printer', views.PrinterViewSet)
router.register(r'print', views.PrintViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
