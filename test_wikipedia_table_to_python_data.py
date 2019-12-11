import json
import sqlite3
from prettytable import PrettyTable

def printMenu():
    print("MENU")
    print("----")
    print("0. EXIT")
    print("1. Show All-Time Table FIFA World Cup Statistics")
    print("2. Number of teams participated per confederation")
    print("3. Teams with active drought time by absences on tournament")
    print("4. Teams with only one final tournament played")
    print("5. Teams finished as champions at least once")
    print("6. Teams finished as runner-up best finish")
    print("7. Teams finished on semifinals as best finish")
    print("8. Teams finished on quarter finals or top 8 as best finish")
    print("9. Teams finished on second round as best finish")
    print("10.Teams finished on first round as best finish")
    print("11. Show details for one team")


def printAllTimeTable():
        #print all table by each row
        print("----------")
        print("All-Time Table FIFA World Cup Statistics")
        t = PrettyTable(['ID','Team', 'Confederation', 'Total Final Tournaments Played', 'Active Streak or Drought', 'Games Played', 'Games Won', 'Games Drawn', 'Two Points per Win Total', 'Actual Points Total', 'Goals Converted'])
        for row in cur.execute('SELECT id, team, confederation, total_final_tournaments_played, active_streak_or_drought, games_played, games_won, games_drawn, two_points_per_win_total, actual_points_total, goals_converted FROM AllTimeStats'):
            t.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]])
        return t
        

def printNumberOfTeamsPerConfederation():
        print("----------")
        print("Number of teams participated per confederation")
        t1 = PrettyTable(['Confederation', 'Number of Teams'])
        for row in cur.execute('SELECT confederation, COUNT(id) AS number_of_teams FROM AllTimeStats GROUP BY confederation ORDER BY number_of_teams DESC'):
            t1.add_row([row[0], row[1]])
        return t1

def printActiveDroughtTeams():
        print("----------")
        print("Teams with active drought time by absences on tournament")
        t2 = PrettyTable(['Team', 'Confederation', 'Active Streak or Drought', 'Total Final Tournaments Played', 'Best Finish'])
        for row in cur.execute('SELECT team, confederation, active_streak_or_drought, total_final_tournaments_played, best_finish FROM AllTimeStats WHERE active_streak_or_drought < 0 ORDER BY active_streak_or_drought ASC'):
            t2.add_row([row[0],row[1],row[2],row[3],row[4]])
        return t2

def printOnlyOneTournamentPlayed():
        print("----------")
        print("Teams with only one final tournament played")
        t3 = PrettyTable(['Team', 'Confederation', 'Active Streak or Drought', 'Best Finish'])
        for row in cur.execute('SELECT team, confederation, active_streak_or_drought, best_finish FROM AllTimeStats WHERE total_final_tournaments_played = 1 ORDER BY active_streak_or_drought ASC'):
            t3.add_row([row[0],row[1],row[2],row[3]])
        return t3

def printChampions():
        print("----------")
        print("Teams finished as champions at least once")
        t4 = PrettyTable(['Team', 'Confederation', 'Active Streak or Drought', 'Total Final Tournaments Played', 'Best Finish', 'Actual Points Total', 'Two Points per Win Total'])
        for row in cur.execute("SELECT team, confederation, active_streak_or_drought, total_final_tournaments_played, best_finish, actual_points_total, two_points_per_win_total FROM AllTimeStats WHERE best_finish LIKE 'Champion%' ORDER BY actual_points_total DESC, two_points_per_win_total DESC"):
            t4.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        return t4

def printRunnerUps():
        print("----------")
        print("Teams finished as runner-up best finish")
        t5 = PrettyTable(['Team', 'Confederation', 'Active Streak or Drought', 'Total Final Tournaments Played', 'Best Finish', 'Actual Points Total', 'Two Points per Win Total'])
        for row in cur.execute("SELECT team, confederation, active_streak_or_drought, total_final_tournaments_played, best_finish, actual_points_total, two_points_per_win_total FROM AllTimeStats WHERE best_finish LIKE 'Runner-up%' ORDER BY actual_points_total DESC, two_points_per_win_total DESC"):
            t5.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        return t5

def printSemiFinalists():
        print("----------")
        print("Teams finished on semifinals as best finish")
        t6 = PrettyTable(['Team', 'Confederation', 'Active Streak or Drought', 'Total Final Tournaments Played', 'Best Finish', 'Actual Points Total', 'Two Points per Win Total'])
        for row in cur.execute("SELECT team, confederation, active_streak_or_drought, total_final_tournaments_played, best_finish, actual_points_total, two_points_per_win_total FROM AllTimeStats WHERE best_finish LIKE 'Third place%' OR best_finish LIKE 'Fourth place%' ORDER BY actual_points_total DESC, two_points_per_win_total DESC"):
            t6.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        return t6

def printQuarterFinalists():
        print("----------")
        print("Teams finished on quarter finals or top 8 as best finish")
        t7 = PrettyTable(['Team', 'Confederation', 'Active Streak or Drought', 'Total Final Tournaments Played', 'Best Finish', 'Actual Points Total', 'Two Points per Win Total'])
        for row in cur.execute("SELECT team, confederation, active_streak_or_drought, total_final_tournaments_played, best_finish, actual_points_total, two_points_per_win_total FROM AllTimeStats WHERE best_finish LIKE 'Top 8%' OR best_finish LIKE 'Quarterfinal%' ORDER BY actual_points_total DESC, two_points_per_win_total DESC"):
            t7.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        return t7

def printSecondRoundFinalists():
        print("----------")
        print("Teams finished on second round as best finish")
        t8 = PrettyTable(['Team', 'Confederation', 'Active Streak or Drought', 'Total Final Tournaments Played', 'Best Finish', 'Actual Points Total', 'Two Points per Win Total'])
        for row in cur.execute("SELECT team, confederation, active_streak_or_drought, total_final_tournaments_played, best_finish, actual_points_total, two_points_per_win_total FROM AllTimeStats WHERE best_finish LIKE 'Second round%' ORDER BY actual_points_total DESC, two_points_per_win_total DESC"):
            t8.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        return t8

def printFirstRoundFinalists():
        print("----------")
        print("Teams finished on first round as best finish")
        t9 = PrettyTable(['Team', 'Confederation', 'Active Streak or Drought', 'Total Final Tournaments Played', 'Best Finish', 'Actual Points Total', 'Two Points per Win Total'])
        for row in cur.execute("SELECT team, confederation, active_streak_or_drought, total_final_tournaments_played, best_finish, actual_points_total, two_points_per_win_total FROM AllTimeStats WHERE best_finish LIKE 'First round%' ORDER BY actual_points_total DESC, two_points_per_win_total DESC"):
            t9.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        return t9

def printOneTeam():
    team = input("Select one team to view details: ")
    print("----------")
    cur.execute('SELECT * FROM AllTimeStats WHERE team LIKE ? LIMIT 1', ('%'+team+'%', ))
    try:
        row = cur.fetchone()
        t10 = PrettyTable(['Team', row[1]])
        t10.add_row(["ID: ",row[0]])
        t10.add_row(["Confederation: ",row[2]])
        t10.add_row(["Total Final Tournaments Played: ",row[3]])
        t10.add_row(["Active Streak or Drought: ",row[4]])             
        t10.add_row(["Games played: ",row[5]])             
        t10.add_row(["Games won: ",row[6]])             
        t10.add_row(["Games drawn: ",row[7]])             
        t10.add_row(["Two Points per Win Total: ",row[8]])
        t10.add_row(["Two Points per Win Average: ",row[9]])
        t10.add_row(["Actual Points Total: ",row[10]])
        t10.add_row(["Actual Points Average: ",row[11]])
        t10.add_row(["Goals converted: ",row[12]])
        t10.add_row(["Best finish: ",row[13]])
        return t10
    except:
        return 'Could not retrieve team '+team


def switchMenu(option):
    switcher = {
        1: printAllTimeTable,
        2: printNumberOfTeamsPerConfederation,
        3: printActiveDroughtTeams,
        4: printOnlyOneTournamentPlayed,
        5: printChampions,
        6: printRunnerUps,
        7: printSemiFinalists,
        8: printQuarterFinalists,
        9: printSecondRoundFinalists,
       10: printFirstRoundFinalists,
       11: printOneTeam
    }
    func = switcher.get(option, lambda: "INVALID OPTION!!!")
    print(func())
    



conn = sqlite3.connect('data/fifa-world-cup.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS AllTimeStats ''')

cur.execute('''CREATE TABLE IF NOT EXISTS AllTimeStats
    (id INTEGER PRIMARY KEY, 
     team VARCHAR UNIQUE, 
     confederation VARCHAR,
     total_final_tournaments_played INTEGER, 
     active_streak_or_drought INTEGER,
     games_played INTEGER, games_won INTEGER, games_drawn INTEGER, 
     two_points_per_win_total INTEGER, two_points_per_win_average FLOAT, 
     actual_points_total INTEGER, actual_points_average FLOAT, 
     goals_converted INTEGER,   
     best_finish TEXT)''')

# read file
with open('data/all-time_fifa_world_cup.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

count = 0
# load keys and values on database
for i in range(len(obj)):
    #print(obj[i])
    team = obj[i]['team']
    confederation = obj[i]['confederation']
    total_final_tournaments_played = int(obj[i]['total_final_tournaments_played'])
    active_streak_or_drought = int(obj[i]['active_streak_or_drought'])
    games_played = int(obj[i]['games_played'])
    games_won = int(obj[i]['games_won'])
    games_drawn = int(obj[i]['games_drawn'])
    two_points_per_win_total = int(obj[i]['two_points_per_win_total'])
    two_points_per_win_average = float(obj[i]['two_points_per_win_average'])
    actual_points_total = int(obj[i]['actual_points_total'])
    actual_points_average = float(obj[i]['actual_points_average'])
    goals_converted = int(obj[i]['goals_converted'])
    best_finish = obj[i]['best_finish']
    cur.execute("INSERT OR IGNORE INTO AllTimeStats  (team, confederation, total_final_tournaments_played, active_streak_or_drought, games_played, games_won, games_drawn, two_points_per_win_total, two_points_per_win_average, actual_points_total, actual_points_average, goals_converted, best_finish) VALUES ( ?,?,?,?,?,?,?,?,?,?,?,?,? )",
            ( team, confederation, total_final_tournaments_played, active_streak_or_drought, games_played, games_won, games_drawn, two_points_per_win_total, two_points_per_win_average, actual_points_total, actual_points_average, goals_converted, best_finish))
    count = count + 1

conn.commit()

print("WELCOME TO ALL-TIME FIFA WORLD CUP STATISTICS APPLICATION!!!")
printMenu()
try:
    option = input("Please, enter an option to do: ")
    while option != "0":
        switchMenu(int(option))
        printMenu()
        option = input("Please, enter an option to do: ")
except:
    print("INVALID OPTION!!! Please enter a number between 0 and 11")
    






































cur.close()