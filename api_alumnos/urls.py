from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from api import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

#Adding endpoints to viewsets
router = routers.DefaultRouter()
router.register('alumnos', views.AlumnoViewSet)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/', include(router.urls)),
    url(r'api/v1/format/alumnos/(?P<pk>[0-9]+)/$', views.AlumnoDetail.as_view()),
]

