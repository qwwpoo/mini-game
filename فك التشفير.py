import string
word=''
list = string.ascii_letters
sant = input('enter the sentans:')
scrit = int(input('enter the scrite number:'))
for num in sant:
 if num in list:
  end=list.index(num)
  new_ind=(end-scrit)%52     
  word += list[new_ind]
 else :
  word += num 
print(word) 