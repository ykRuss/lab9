from django.contrib import admin
from django.urls import path, include
from app_name import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('movies/', include('app_name.urls')),  
]
