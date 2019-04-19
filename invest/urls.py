from django.urls import path
from . import views
app_name = 'invest'
urlpatterns = [
    path('invest/<int:projects_id>/', views.invest, name='invest'),
    path('invest/start/', views.start, name='start'),
]