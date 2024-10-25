# Generated by Django 4.1.3 on 2022-11-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WinnerPick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.IntegerField(null=True)),
                ('player', models.CharField(choices=[('Renee', 'Renee'), ('Mr. C.', 'Mr. C.'), ('Tiara', 'Tiara')], max_length=200, null=True)),
                ('away', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Buffalo Bills', 'Buffalo Bills'), ('Chicago Bears', 'Chicago Bears'), ('Carolina Panthers', 'Carolina Panthers'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Denver Broncos', 'Denver Broncos'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Jacksonville Jaguars', 'Jacksonvile Jaguars'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Miami Dolphins', 'Miami Dolphins'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New England Patriots', 'New England Patriots'), ('New York Giants', 'New York Giants'), ('New York Jets', 'New York Jets'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seatle Seahawks', 'Seatle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Tennessee Titans', 'Tennessee Titans'), ('Washington Commanders', 'Washington Commanders')], max_length=200, null=True)),
                ('home', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Buffalo Bills', 'Buffalo Bills'), ('Chicago Bears', 'Chicago Bears'), ('Carolina Panthers', 'Carolina Panthers'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Denver Broncos', 'Denver Broncos'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Jacksonville Jaguars', 'Jacksonvile Jaguars'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Miami Dolphins', 'Miami Dolphins'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New England Patriots', 'New England Patriots'), ('New York Giants', 'New York Giants'), ('New York Jets', 'New York Jets'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seatle Seahawks', 'Seatle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Tennessee Titans', 'Tennessee Titans'), ('Washington Commanders', 'Washington Commanders')], max_length=200, null=True)),
                ('away_score', models.IntegerField(default=0, null=True)),
                ('home_score', models.IntegerField(default=0, null=True)),
                ('selected_pick', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Buffalo Bills', 'Buffalo Bills'), ('Chicago Bears', 'Chicago Bears'), ('Carolina Panthers', 'Carolina Panthers'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Denver Broncos', 'Denver Broncos'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Jacksonville Jaguars', 'Jacksonvile Jaguars'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Miami Dolphins', 'Miami Dolphins'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New England Patriots', 'New England Patriots'), ('New York Giants', 'New York Giants'), ('New York Jets', 'New York Jets'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seatle Seahawks', 'Seatle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Tennessee Titans', 'Tennessee Titans'), ('Washington Commanders', 'Washington Commanders')], max_length=250, null=True)),
                ('actual_winner', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Buffalo Bills', 'Buffalo Bills'), ('Chicago Bears', 'Chicago Bears'), ('Carolina Panthers', 'Carolina Panthers'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Denver Broncos', 'Denver Broncos'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Jacksonville Jaguars', 'Jacksonvile Jaguars'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Miami Dolphins', 'Miami Dolphins'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New England Patriots', 'New England Patriots'), ('New York Giants', 'New York Giants'), ('New York Jets', 'New York Jets'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seatle Seahawks', 'Seatle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Tennessee Titans', 'Tennessee Titans'), ('Washington Commanders', 'Washington Commanders')], max_length=250, null=True)),
                ('status', models.CharField(choices=[('Win', 'Win'), ('Lose', 'Lose'), ('Tie', 'Tie')], max_length=6, null=True)),
            ],
            options={
                'ordering': ['-week_number', 'player'],
            },
        ),
    ]