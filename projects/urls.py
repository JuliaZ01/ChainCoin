from django.urls import path

from . import views
app_name = 'projects'
urlpatterns = [
    path('start/', views.start, name='start'),
    path('detail/<int:projects_id>/', views.detail, name='detail'),
    path('show/', views.show, name='show'),
]