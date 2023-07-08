from django.urls import path
from . import views

urlpatterns = [

    path('form/', views.teamform, name='team'),
    path('', views.homeawayview, name='select_week'),
    path('final/', views.print_final, name='final'),
    path('winner/', views.winnerPick, name='winner'),
    path('total/',views.total, name='total'),
    path('winners/', views.print_winners,name='print_winners'),
    path('print_week/',views.print_week,name='week'), # Added 7/7/2023 - lets get the player and total points and the week to pring.
    path('<int:week_number>/',views.printWeek, name='print_week'),
        
   
    
]