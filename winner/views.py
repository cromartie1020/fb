from django.shortcuts import render
from teams.models import Home_Away
from teams.forms import Home_Away, HomeAwayForm, WinnerPickForm



def select_winners(request):
   
    week_number=request.GET.get('week_number')
    player=request.GET.get('player')
    
    selections=Home_Away.objects.filter(week_number=week_number)
    
    week_number=request.GET.get('week_number')
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    total=home_aways.count()
    form=WinnerPickForm()


    context = {
        
        'form':form,
        'week_number':week_number,
        'home_aways':home_aways,
        'total':total,
        
    
    }
    