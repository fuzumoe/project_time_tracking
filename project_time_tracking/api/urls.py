from django.urls import path, include
from rest_framework import routers, viewsets
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from project_time_tracking.api.views.users_view import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('schema', SpectacularAPIView.as_view(), name="schema"),
    path('docs',
         SpectacularSwaggerView.as_view(
             template_name='swagger-ui.html', url_name='schema'
         ),
         name="swagger-ui",
         ),
]
