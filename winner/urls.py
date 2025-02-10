from django.urls import path 
from . import views
urlpatterns = [
    path('', views.select_winners, name='select_winners')
]