"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView

from chart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('w', TemplateView.as_view(template_name='w.html'), name='w'),
    path('ws', views.ws, name='ws'),
    path('age', TemplateView.as_view(template_name='age.html'), name='age'),
    path('ages', views.ages, name='ages'),
    path('genders', views.genders, name='genders'),
    path('genders2', views.genders2, name='genders2'),
    path('traffic', TemplateView.as_view(template_name='traffic.html'), name='traffic'),
    path('traffics', views.traffics, name='traffics'),
]
