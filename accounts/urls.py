from django.urls import path

from . import views
app_name = 'accounts'
urlpatterns = [
    # 我的项目
    path('', views.index, name='index'),
    path('settle', views.settle, name='settle'),
    # 我的捐赠
    path('donate', views.donate, name='donate'),
]