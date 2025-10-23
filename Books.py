import os
lanrary = {}

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def add():
  while True:
    clear()
    icpn = input('enter the icpn: ')
    au = input('enter the name author: ')
    addr = input('enter the address: ')
    lanrary[icpn] = {'icpn': icpn, 'author': au, 'addrass': addr, 'avaliable': True}
    print('operation successfully done')
    print('Book info:', 'Address:', lanrary[icpn]['addrass'], 'Author:', lanrary[icpn]['author'],
          'ICPN:', lanrary[icpn]['icpn'], 'Available:', True)
    ask = input('do you need to add another book (y/n)? ').lower()
    if ask != 'y':
      break

def check_out():
  while True:
    clear()
    icpn = input('enter the icpn: ')
    if icpn in lanrary:
      if lanrary[icpn]['avaliable']:
        lanrary[icpn]['avaliable'] = False
        print('okey, the book is checked out')
      else:
        print('sorry, this book is already checked out')
    else:
      print('sorry, this book not found')
    ask = input('do you need another check out (y/n)? ').lower()
    if ask != 'y':
      break

def check_in():
  while True:
    clear()
    icpn = input('enter the icpn: ')
    if icpn in lanrary:
      if not lanrary[icpn]['avaliable']:
        lanrary[icpn]['avaliable'] = True
        print('okey, the book is checked in')
      else:
        print('this book is already available')
    else:
      print('sorry, this book not found')
    ask = input('do you need another check in (y/n)? ').lower()
    if ask != 'y':
      break

def view():
  while True:
    clear()
    print('Library Catalog:')
    for icpn in lanrary:
      book_info = lanrary[icpn]
      print('ICPN:', icpn,
            'Address:', book_info['addrass'],
            'Author:', book_info['author'],
            'Available:', book_info['avaliable'])
    choice = input('Press Enter to return to main menu ')
    break

while True:
  print('\nMenu:')
  print('1 - Add Book')
  print('2 - Check Out Book')
  print('3 - Check In Book')
  print('4 - List Books')
  print('5 - Exit')
  ask = int(input('Enter your choice: '))
  if ask == 1:
    add()
  elif ask == 2:
    check_out()
  elif ask == 3:
    check_in()
  elif ask == 4:
    view()
  elif ask == 5:
    print('Exiting program...')
    break
  else:
    print('Invalid choice, please enter a number between 1 and 5')