from django.urls import path
from . import views

urlpatterns = [

    path('form/', views.teamform, name='team'),
    path('', views.homeawayview, name='select_week'),
    path('final/', views.print_final, name='final'),
    #path('', views.select_your_picks, name='picks'),
    path('winner/', views.winnerPick, name='winner'),
    path('total/',views.total, name='total'),
    path('winners/', views.print_winners,name='print_winners'),
    path('<int:week_number>/',views.printWeek, name='print_week'),
    #path('', views.select_week, name='select_week'),
        
   
    
]