import random 
words = ['ahmed','mhmod','karym','bad','agly','happy','sad','hungry']
chose = random.choice(words)
#=====خنا قوائم ومتغيرات=======
wrong = []
list=[]
lives = 6
mine = len(chose)
hang =['''|''',
'''
     |___
''',
'''
     |
    _|___
''',
'''     |   
     |      
     |
    _|___''',
'''
     |       |
     |      /\
     |
    _|___
''',
'''
     |      \|/
     |       |
     |      / \
     |
    _|___''',
'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___''']
# بداية العبه
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      ''')
#------------------------------
print('''    _______
            |/    
            |      
            |     
            |      
            |      
            |''')
#==============================
#هنا هنبدا بي عمل الفائمه
list = ['_']*len(chose)
print(' '.join(list)) 
#==============================
#هنا بيدخل الحروف في اماكنها الصحيحه
def loop():
 for i in range(mine) :
  if chose[i] == ask:
   list[i] = ask
 print(' '.join(list))
#هنا احنا هنعدد عدد المحاولات و القلوب
while '_'  in list and lives > 0 :
 ask = input('inter the caracter').lower() 
 if ask not in chose :
  if ask in wrong :
   print('you aiready gussed that,try again.')
   continue 
  lives-=1 
  v = 6-lives
  print(hang[v])
  #-----------------
  #_________________
  print('choice is wrong your lives is',lives)
  wrong.append(ask)
  loop() 
  if lives == 0:
   print('your write choice is:(',chose,')')
 elif ask in chose:  
  loop()
  print('your choice is very good')
if '_' not in list:
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++									 
 print('''*****************
          _       
         (_)      
__      ___ _ __  
\ \ /\ / / | '_ \ 
 \ V  V /| | | | |
  \_/\_/ |_|_| |_|
                  
 ****************''')
 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



