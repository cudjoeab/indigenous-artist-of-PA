"""indartspa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from indartspa import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^$', views.all_submissions, name='submission'),
    url(r'^$', views.new_submission, name='new_submission'),
    # path('', views.home, name='home'),
    # path('admin/', admin.site.urls),
    # path('submissions/', views.all_submissions, name= 'submissions'),
    # path('new_submission/', views.new_submission, name='new_submission'),
    # path('artists/', views.artists, name='artists'), 
]
