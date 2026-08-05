from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('send_alert/', views.send_alert_page, name='send_alert_page'),  # GET page
    path('api/send_alert/', views.send_alert_api, name='send_alert_api'),  # POST JSON
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
]
