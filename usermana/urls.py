from django.urls import path

from . import views
app_name = 'usermana'
urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('scharge/', views.scharge, name='scharge'),
]