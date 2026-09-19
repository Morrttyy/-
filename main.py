from data_manager import (insert_game, insert_player, get_games, get_best_attempts, get_top_three_players)
import random

def player_info():
    x=input('lotfan esmet ro begoo?').strip()
    y=input(('lotfan cod mellit ro beggo')).strip()
    return y, x

def input_number():
    y=random.randint(1, 20)
    while True :
        try :
            x=int(input('ye adad begoo?'))
            if 0 < x < 21:
                return x, y
            else:
                raise Exception
        except Exception:
           print('lotfan adad monaseb vared konid')

def compare(x, y):
    if x > y :
        print('bia paain')
        return False
    if x < y :
        print('boro bala')
        return False
    return True
        
def dobareh():
    x=input('az avval ?')
    if x == 'y':
        print('pas berim...')
    if x =='n':
        return True
def play_game():
    x, y = input_number()
    attempts = 1
    while not compare(x, y):
        x=int(input('dobareh begoo'))
        attempts += 1
    print(f'affarin adad dorost {y} bood . va to {attempts} ta hads gofti')
    return attempts

def menu():
    print('\n====================')
    print('        MENU')
    print('====================')
    print('1. start playing')
    print('2. my best record')
    print('3. my game history')
    print('4. three top player of the game')
    print('5. exit')

    choice = input('choice :  ').strip()

    return choice

def show_my_games(NA_id):
    games = get_games(NA_id)
    if not games:
        print('\nhanooz bazi barat sabt nashodeh.')
        return

    print('\n====================')
    print('     my history')
    print('====================')

    for game in games:
        game_id, NA_id, attempts, played_at = game

        print(f'\n shomare anjam bazi: {game_id}')
        print(f'tedad talash: {attempts}')
        print(f'tarikh va zaman: {played_at}')
        print('--------------------')

def show_top_three():
    top_players = get_top_three_players()

    if not top_players:
        print('\nhanooz recordi baraye rotbe bandi vojod nadarad.')
        return

    print('\n====================')
    print('     three top player')
    print('====================')

    for rank, player in enumerate(top_players, start=1):
        name, best_attempts = player

        print(f'{rank}. {name} 'f'→ best: {best_attempts} try')
    
def main():
    NA_id, name = player_info()
    result = insert_player(NA_id, name)
    if result == 'diffrent_name':
        print(' in code melli ghablan ba name digari sabt shodeh ast')
        return 
    
    while True:
        choice = menu()
        if choice == '1':
            attempts = play_game()
            insert_game(NA_id, attempts)
        elif choice == '2':
            best_attempts = get_best_attempts(NA_id)

            if best_attempts is None:
                print('\n hanooz bazi nakardi.')
            else:
                print(f'\nbehtarin record shoma: 'f'{best_attempts} ')

        elif choice == '3':
            show_my_games(NA_id)

        elif choice == '4':
            show_top_three()

        elif choice == '5':
            print('\nbye')
            break

        else:
            print('\ndorost entehkab kon.')
    
if __name__ == '__main__':
    main()
   