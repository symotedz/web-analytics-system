"""
URL configuration for Analytics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
cv c f    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls',namespace='api')),
    path('api_accountant/', include('api_accountant.urls', namespace='api_accountant')),
    path('api_admin/', include('api_admin.urls', namespace='api_admin')),
    path('api_librarian/', include('api_librarian.urls', namespace='api_librarian')),
    path('api_parent/', include('api_parent.urls', namespace='api_ parent')),
    path('api_student/', include('api_student.urls', namespace='api_student')),
    path('api_super_admin/', include('api_super_admin.urls', namespace='api_super_admin')),
    path('api_teacher/', include('api_teacher.urls', namespace='api_teacher')),
    # path('parent/', include('parent.urls')),
    # GLOBAL URLS FOR WEB ADMIN
    path('accountant/', include('web_accountant.urls', namespace='web_accountant')),
    path('web_admin/', include('web_admin.urls', namespace='web_admin')),
    path('app/', include('web_app.urls', namespace='web_app')),
    path('librarian/', include('web_librarian.urls', namespace='web_librarian')),
    path('parents/', include('web_parents.urls', namespace='web_parents')),
    path('student/', include('web_student.urls', namespace='web_student')),
    path('super_admin/', include('web_super_admin.urls', namespace='web_super_admin')),
    path('teacher/', include('web_teacher.urls', namespace='web_teacher')),

    # Urls for Other Core System Modules
    path('socialmedia/', include('socialmedia.urls', namespace="socialmedia")),
    path('dataAnalysis/', include('dataAnalysis.urls', namespace='dataAnalysis')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)