"""Report URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ReportingApp import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #path('admin/index.html/',views.dashboard),
    path('admin/dashboard/',views.dashboard),
    #path('admin/calc/',views.calc),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('admin/home/',views.home),
    path('admin/home/addnew/',views.addnew),
    path('admin/home/addnew/upload',views.upload),
    # url(r'^report_builder/', include('report_builder.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
