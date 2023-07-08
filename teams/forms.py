from django import forms
from .models import Team, Home_Away, WinnerPick
from django.db import models


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class HomeAwayForm(forms.ModelForm):
    class Meta:
        model = Home_Away
        fields = ['week_number', 'away_team',
                  'home_team', 'startdate', 'starttime']
        widgets = {'startdate': DateInput(), 'starttime': TimeInput()}


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']



class WinnerPickForm(forms.ModelForm):
    class Meta:
        model = WinnerPick
        fields = ['week_number','player','away','home','away_score','home_score','selected_pick','actual_winner','status']

