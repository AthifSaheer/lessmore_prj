from django.urls import path
from .import views
urlpatterns = [
    path('address', views.address, name='address')
]