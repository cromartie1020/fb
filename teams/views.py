from django.shortcuts import render, redirect
from . forms import HomeAwayForm, TeamForm, WinnerPickForm,WinnerSelectForm
from .models import Team, Home_Away,WinnerPick
from players import PLAYERS,Players # Players in the pool
from django.contrib.auth.decorators import login_required

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
    if request.method == ('POST' or None):
        form = WinnerPickForm(request.POST)                                    
        if form.is_valid():
            week_number=form.cleaned_data['week_number']
            print(week_number)
            form.save()
            return redirect('select_week')
    else:
        form=WinnerPickForm()
    
    context={
        "form":form,
       
    }
    
    return render(request,'teams/select_your_picks.html', context)

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
    
    
      
    return render(request, 'teams/select_winners.html', context)    

def print_week(request):  # This function added 7/7/2023 to replace printweek function
    week_number=request.GET.get('week_number')
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    
    
    
    context = {
        'home_aways':home_aways,
        'week_number':week_number,
         
        


    } 
    
           

    return render (request,'teams/print_week.html', context)



def confirm_selections(request):
    # List our selections from HomeAway and show an option 
    # to edit my choices.
    week_number=request.GET.get('week_number')
    year = request.GET.get('year') 
    #year = request.GET.get((year)
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

def update(request, id):
    list = WinnerPick.objects.get(id=id)
    form = WinnerPickForm(instance = list)
    if request.method==('POST' or None):
        form = WinnerPickForm(request.POST, instance = list)
        if form.is_valid():
            form.save()
            return redirect('list')


    context = {
        'form':form,
    }
    return render(request,'teams/select_your_picks.html',context )

def winnerPickNew(request, id):
    list = WinnerPick.objects.get(id=id)
    form = WinnerPickForm(instance=list)
    if request.method ==('POST' or None):
        week_number   = request.GET['week_number']
        year          = request.GET['year']
        player        = request.GET['player']
        away          = request.GET['away']
        home          = request.GET['home']
        away_score    = request.GET['away_score']
        home_score    = request.GET['home_score']
        actual_winner = request.GET['actual_winner']
        status        = request.GET['status']
        WinnerPick.objects.create(week_number=week_number,year=year,player=player,away=away,home=home,away_score=away_score,home_score=home_score,actual_winner=actual_winner,status=status)
        return redirect('list')
    context = {
        'form':form,
    }
    return render(request, 'teams/select_your_picks.html', context)
    
    
def winnerPickList(request):
    list=WinnerPick.objects.all()
    context = {
        'list':list,
    }
    return render(request, 'teams/winnerPickList.html', context)

def print_player_week_selections(request):
    form =WinnerPickForm()
    if request.method=='POST':
        week_number = request.POST['week_number']
        year        = request.POST['year']
        player      = request.POST['player']
        winners     = WinnerPick.objects.filter(week_number__icontains=week_number).filter(year__icontains=year).filter(player__icontains=player)
        for winner in winners:
            print(winner.home)
        context={
            'winners':winners,
        }    
        return render(request,'teams/print_selected_winners.html', context)    
    context ={
        'form':form,
        'players':Players,
        #'winners':winners    
    }
    return render(request,'teams/print_player_week_selections.html', context)

def pick_winner_list(request):
    week_number=request.GET.get('week_number')
    year = request.GET.get('year') 
    player = request.GET.get('player')
    
    context={
        'week_number':week_number,
        'year'       :year,
        'players'     :Players,
        
    }    
    return render(request,'teams/print_player_week_selections.html',context)

