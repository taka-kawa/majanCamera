from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.test, name='test'),
    path('detection/', views.detection, name='detection')
]
