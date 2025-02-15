from django.shortcuts import render, redirect
from . forms import HomeAwayForm, TeamForm, WinnerPickForm,WinnerSelectForm
from .models import Team, Home_Away,WinnerPick
from players import PLAYERS,Players # Players in the pool
from django.contrib.auth.decorators import login_required
from pathlib import Path
# Add a new Team.
def teamform(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()

        form = TeamForm()
    return render(request, 'teams/team.html', {'form': form})

def homeawayview(request):
    teams = Team.objects.all()
    form = HomeAwayForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = HomeAwayForm()
        redirect('winner')
    else:
        form = HomeAwayForm()
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

def winnerPick(request):  # Lets select the winner from a particular week
    form = WinnerPickForm(request.POST or None)
    if form.is_valid():
        print(request.POST['home'])
        print(request.POST['status'])
        form.save()
        return redirect('winner')
    
    form=WinnerPickForm()
    context={
        "form":form
    }
    return render(request,'teams/select_your_picks.html', context)
#----------------------new 2/13/2025----This function is  not being use.-----------------------
def selectWinners(request):
    week_number=request.GET.get[week_number]
    year = request.GET.get[year]
    print(week_number, year)
    print('testing')
    home_aways=Home_Away.objects.filter(week_number=week_number).filter
    home_away = Home_Away.object.first()
    Home_Away=Home_Away.objects.exclude(home_away)
    print(home_away)
    context = {
        'home_away':home_away
    }
    return render(request, 'base/select_winners.html', context) 
#------------------------------------------------------------------------------------------------

def total(request):
    pass

def print_winners(request):
    return render(request, 'teams/print_winners.html')

def printWeek(request,week_number  ):  # We also need to check the year.
    
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    total=home_aways.count()

    context = {
        'home_aways':home_aways,
        'week_number':week_number,
        'total':total       
    } 
    return render (request,'teams/print_week.html', context)

#------Function is being used---------------------------------------------
def select_winners(request):
    week_number=request.GET.get('week_number')
    player=request.GET.get('player')
    year = request.GET.get('year')
    # a='home'
    # if a.exist():
    # if file exist read info for selections
    # else write selection to file
    selections=Home_Away.objects.filter(week_number=week_number).filter(startdate__contains=year).first()
    home_aways=Home_Away.objects.filter().exclude(home_team__icontains=selections.home_team).exclude(away_team__icontains=selections.away_team)
    
    id = selections.id
    
        
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime').exclude(id =id)
    
    print( selections )
    print()
    print()
    print(home_aways)
    
    '''
    for home_away in home_aways:
        temp.append(home_away)
        tempId.append(home_away.id)
    for x in  range (2,home_aways.count()):
        print (temp[x])    
        print(tempId[x])
    with open('home','w') as file:
        for home_away in home_aways:
            file.write(home_away.away_team)
            file.write(' and ') 
            file.write(home_away.home_team) 
            file.write('   ')     
            file.write(str(home_away.id))
            file.write('\n')
    '''               
    form=WinnerPickForm()
    
    context = {
        'form':form,
        'week_number':week_number,
        'home_aways':home_aways,
        'total':total,
    }
    return render(request, 'teams/select_winners.html', context)    
#------------------------------------------------------------------------------------------------------------

#--------------------------This function is being used to print the week-------------------------------------   

def print_week(request):  # This function added 7/7/2023 to replace printweek function
    week_number=request.GET.get('week_number')
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')

    context = {
        'home_aways':home_aways,
        'week_number':week_number,
    } 
    return render (request,'teams/print_week.html', context)
#------------------------------------------------------------------------------------------------------------


def confirm_selections(request):
    # List our selections from HomeAway and show an option 
    # to edit my choices.
    week_number=request.GET.get('week_number')
    year = request.GET.get('year') 
    selections=Home_Away.objects.filter(week_number=week_number)
    week_number=request.GET.get('week_number')
    home_aways = Home_Away.objects.filter(week_number=week_number).filter(startdate__year=year).order_by('startdate','starttime')
    
    # ______Lets find a way to determine the teams on a bye. _____________________________
    #_____________________________________________________________________________________

    context={
        'selections':selections,
        'week_number':week_number,
        'home_aways':home_aways,
        'year':year,
    }
    return render(request, 'teams/print_week.html',context)  

def pick_week(request):
    context = {
        "players":Players,
    }
    return render(request,'teams/pick_week.html', context)

def save_winners(request):
    print('request', request)
    pick=request.GET.get('8')
    print('pick',pick)
    context={
        "pick":pick,

    }
    return render(request, 'teams/winners_saved.html',context)

@login_required
def winner_select_view(request):
    week_number=request.GET.get('week_number')
    print('week_number:',week_number)
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    print ('home_aways:',home_aways)
    #form=WinnerSelectForm()
    context={
        "teams":home_aways,
        #"form":form,
    }
    return render(request,'teams/select_winners.html',context)

