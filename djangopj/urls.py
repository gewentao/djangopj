"""djangopj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import mainPage
from blog.views import postPage
from blog.views import archivePage
from blog.views import galleryPage
from blog.views import aboutPage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',mainPage),
    url(r'^archive/$',archivePage),
    url(r'^gallery/$',galleryPage),
    url(r'^about/$',aboutPage),
    url(r'^blog/post',postPage),
]

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()
