
from django.contrib import admin
from django.urls import path

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    #en la siguiente linea cambien el 10/09 el name="home" por name="HomeView"
    path('', HomeView.as_view(), name="home"),
    path('<slug:cadenaid>/', HomeView.as_view(), name="home-slug"),
]
