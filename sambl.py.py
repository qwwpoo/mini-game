print('****welcome in math*****')
list=[]
listt=[]
ask = int(input('how many items are there in your basket today?'))
print("let's get to cantery them\n") 
for i in range(1,ask+1):
 name = input('plese tell me the item number''\n').lower()
 list.append(name)
 number = float(input('what is the price of''\n'))
 listt.append(number)
show = input('would you like to see your entire basket items?').lower()
if show == 'yes':
 print(list)
 user = input ("would you like to see how much it'll cost?").lower()
 if user == 'yes':
  print('\n')
  print('puying these items will cost:') 
  print(sum(listt))  