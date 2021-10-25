""" intro = input("enter your complete details... ")
count = 0
wordCount = 1


for i in intro:
    count+=1
    if (i == " ") :
      wordCount+=1 """


""" list = [1,2,3,4,5]
count = 0

firstNum = list[0]

list[0] = list[len(list)-1]
list[len(list)-1] = firstNum

print(list) """

""" num = 10 
while (num>=0) :
  print(num)
  num-=1 """

""" num1 = 10

for i in range(num1, -1, -1):
  print(i) """


""" for i in range(0,exchangeTill,1):
  firstNum = word[i]

  word[i] = word[len(word)-1]
  word[len(word)-i] = firstNum """

  
word = input("enter a word ")
reversedWord=""


for i in word:
  reversedWord = reversedWord+i
  print(reversedWord)

if (word == reversedWord):
  print('its a palindrome')
else : 
  print('its a not palindrome')

  




""" I am tina --- I need to count 
the no of word not the no of letters and we need to use the if condition in the for loop
  """

""" interchange the first and the last number of the list - whenever we are asked to swipe the valuyes then always we have to first assign the first
value of the list to a var and then have to assign the last value to the first value"""