import random 
import time 
import os 
def asc():
 print('''          _             _                                 _     
  _     _            _    _            _    
 | |   | |          | |  (_)          | |   
 | |__ | | __ _  ___| | ___  __ _  ___| | __
 | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   <| | (_| | (__|   < 
 |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                        _/ |                
                       |__/                 
  ''')
 print(''' 
           _____
          |A .  | _____
          | /.\ ||A ^  | _____
          |(_._)|| / \ ||A _  | _____
          |  |  || \ / || ( ) ||A_ _ |
          |____V||  .  ||(_'_)||( v )|
                 |____V||  |  || \ / |
                        |____V||  .  |
                               |____V|''')
def cls() :
 os.system('cls') if os.name == 'nt' else os.system('clear')

def cards():
  list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(list)  
  return card

def calcoltion(card):
 """تاخد قائمه من الكروت وتجمعهم"""
 if sum(card) == 21 and len(card) == 2: #هل يوجد بالك جالك ام لا
  return 0
 if 11 in card and sum(card) > 21: #هل كروت المستخدم اكبر من 21 وفيها 11
  card.remove(11)
  card.append(1)
 return sum(card) 

def diffrint(user_scor,computer_scor):
 dec = {
 'blakgak_player' : 'Congratulations, you got a Blackjack.',
 'player_big' : 'You lose because your score is over 21.',
 'computer_big' : 'You win, the computer went over 21.',
 'draw' : 'It is a draw.',
 'blackgak_com' : 'You lose, the computer got a Blackjack.',
 'player_win' : 'You win.',
 'computer_win' : 'You lose.',

 }
 if user_scor == computer_scor :
  return dec['draw']
 elif user_scor == 0:
  return dec['blakgak_player'] 
 elif computer_scor == 0:
  return dec['blackgak_com']
 elif user_scor > 21:
  return dec['player_big']
 elif computer_scor > 21 :
  return dec['computer_big'] 
 elif user_scor > computer_scor :
  return dec['player_win']
 else:
  return dec['computer_win']

def game() :
  player =[cards()for _ in range(2)]
  computer =[cards()for _ in range(2)]
  n = True 
  while n :
   user_scor = calcoltion(player)
   computer_scor = calcoltion(computer)
   print('\n\n\n your cards are  ',player,'corrent scor is',sum(player))
   print('computer is first card',computer[0])
   if user_scor == 0 or computer_scor == 0 or sum(player) > 21 or sum(computer) > 21:
    n = False
    break	
   else:
    user_need_anthir_card = input('gat a nothir card?:').lower()
    if user_need_anthir_card == "y":
     print('......')
     time.sleep(1)
     cls()
     player.append(cards())
    else:
     cls()
     print('\n')
     n = False 
     break	 
  while computer_scor != 0 and computer_scor < 17 :
   computer.append(cards())
   computer_scor = calcoltion(computer)
  print('your final hand:',player,'with scor',user_scor)
  print('computer "s final hand',computer,'with score ',computer_scor)   
  print(diffrint(user_scor,computer_scor))  
asc()
me=input('choose a game to star ....\n\nfroggy\ntwenty one\nsnake\n').lower() 
while me == 'twenty one' or me == '21':
 print('okey....')
 time.sleep(2)
 cls()
 asc()
 game()  
 if input('you need a try play agean ?(y/n)') == 'y':
  continue
 else:
  break 
   