"""project URL Configuration

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
from django.conf.urls import url, include
from profiles import views as profile_views
from django.conf import settings
from django.conf.urls.static import static
from checkout import views as checkout_views



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    path('', profile_views.Home, name='home'),
    path('profile/', profile_views.profileview, name='profile'),
    path('contact/', profile_views.contactview, name='contact'),
    path('checkout/', checkout_views.checkoutview, name='checkout'),
    path('charge/', checkout_views.charge, name='charge'),
    path('success/<str:args>/', checkout_views.successMsg, name='success'),
    path('premium/', checkout_views.premium, name='premium'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

