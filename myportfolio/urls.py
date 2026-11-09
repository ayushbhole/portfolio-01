"""
URL configuration for myportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myportfolio import views
from django.urls import path, include 
from .views import chatbot_view
from django.conf import settings
from django.    conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('Home/',views.Homepage),
    # path('',views.Homepage),
    # path('about/',views.about),
    #path('contact/',views.Contact),
    # path('captcha/', include('captcha.urls')),
    # path('portfolio/',views.portfolio),
    # path('', views.portfolio, name='portfolio'),
    # # path("chatbot/", chatbot_view, name="chatbot"),
    # path('', include('myportfolio.urls')),
    
    
    
    path('admin/', admin.site.urls),
    # Path for the django-simple-captcha library
    path('captcha/', include('captcha.urls')),
    # Portfolio view (The main landing page)
    # The '' path is handled by views.portfolio
    path('', views.portfolio, name='portfolio'),
    
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
