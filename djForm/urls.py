from django.contrib import admin
from django.urls import path, include
from examapp.views import home, about, contact, register 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]