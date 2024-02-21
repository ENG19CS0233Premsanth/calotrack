"""
URL configuration for calotrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from calapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.calview),
    path('addcontent/',views.addcontent,name='addcontent'),
    path('chcontent/',views.chview,name='chcontent'),
    path('admin/', admin.site.urls),
    path('delete/<int:pk>',views.del1,name='delete'),
    path('new/<int:pk>',views.new,name='new'),
    path('update/<int:pk>',views.upd,name='upd')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
