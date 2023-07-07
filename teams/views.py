from django.shortcuts import render, redirect
from . forms import HomeAwayForm, TeamForm, WinnerPickForm
from .models import Team, Home_Away

def select_week(request):
    pass

def teamform(request):
    form = TeamForm(request.POST or None)
            
    if form.is_valid():
        form.save()

        form = TeamForm()

    return render(request, 'teams/team.html', {'form': form})


def homeaway(request):
    pass

def homeawayview(request):
    teams = Team.objects.all()
    form = HomeAwayForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = HomeAwayForm()
        redirect('winner')

    else:
        form = HomeAwayForm()
        print('This is a test.')

    return render(request, 'teams/select_teams.html', {'form': form, 'teams': teams})

def print_final(request):
    winners=WinnerPick.objects.all()
    context = {
        "winners":winners,
        "players":PLAYERS
    }
    return render(request, 'teams/final.html',context)

def select_your_picks(request):
    pass

def winnerPick(request):
    form = WinnerPickForm(request.POST or None)
     
    
    if form.is_valid():
        print(request.POST['home'])
        print(request.POST['status'])
        form.save()
        return redirect('winner')
    
    
    context={
        "form":form
    }
    
    return render(request,'teams/select_your_picks.html', context)

def total(request):
    pass

def print_winners(request):
    pass

def printWeek(request,week_number  ):
    
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    
    
    if week_number == 7:
        byes = ['Buffalo,','LA Rams,','Minnesota,','Philadelphia'] 
    if week_number == 6:
        byes = ['Detroit,','Houston,','Las Vegas','Tennessee'] 
            
    else:
        byes=''    
    context = {
        'home_aways':home_aways,
        'week_number':week_number,
         
        'byes':byes


    } 
    
           

    return render (request,'teams/print_week.html', context)
def select_winners(request,week_number):
    home_aways=Home_Away.objects.filter(week_number__exact = week_number)
    for home_away in home_aways:
        print(home_away.away_team,home_away.home_team, home_away.id)
        
    form=WinnerPickForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
    
     
    context = {
        
        'form':form
        
    
    }
    
    form=WinnerPickForm()
    
      
    return render(request, 'yourteams/select_your_picks.html', context)    
