from django.urls import path

from . import views

app_name = 'funds'
urlpatterns = [
        path('', views.index, name = 'index'),
        path('details/<int:funds_id>/', views.detail, name = 'detail'),
        path('overlap', views.overlap, name = 'overlap')
        ]
