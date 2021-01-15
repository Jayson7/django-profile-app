
from django.contrib import admin
from django.urls import path
from mini import views
from mini.views import HomeView, staffs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView, name='home'),
    path('staffs', staffs.as_view(), name='staffs'),
    
]
