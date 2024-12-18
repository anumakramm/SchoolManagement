from django.urls import path
from schoolapp import views

app_name = 'schoolapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),  
]

