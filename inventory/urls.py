from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include,path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import dashboard
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Solidality Fund API",
      default_version='v1',
      description="Solidaty Rest Api",
      contact=openapi.Contact(email="emma@test.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard,name='dashboard'),
    path('sofu/', include('backend.urls')),
    path("accounts/auth/", include("django.contrib.auth.urls")),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
