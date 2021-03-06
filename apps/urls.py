import django
from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('Register', views.register, name='register'),
    path('Login', views.login, name='login'),
    path('crop-api/<int:n>/<int:p>/<int:k>/<int:temp>/<int:humidity>/<int:soilph>/<int:rainfall>/', views.apiview, name='TheApiView'),
  
]

