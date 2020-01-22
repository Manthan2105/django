"""MySite URL Configuration

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
from django.conf.urls import include, url
from MedicStores import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^index/',views.index,name='index'),
    url(r'^$',views.index,name="index"),
    url(r'^checkout/',views.checkout,name='checkout'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^about/',views.about,name='about'),
    url(r'^disclaimer/',views.disclaimer,name='disclaimer'),
    url(r'^shipping/',views.shipping,name='shipping'),
    url(r'^privacy/',views.privacy,name='privacy'),
    url(r'^term/',views.term,name='term'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^sitemap/ ',views.sitemap,name='sitemap'),
    url(r'^client_register/',views.client_register,name='client_register'),
    url(r'^client_login/',views.client_login,name='client_login'),
    url(r'^client_logout/',views.client_logout,name='client_logout'),



]
