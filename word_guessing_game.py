import random
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
Input=input("What is your name? ")
print(f"Good Luck! {Input}")
computer_selector=''
dic={}
lst=[]
a=12
b=True
while a>0 and b==True:
  computer_selector=random.choice(words)
  for i in range(len(computer_selector)):
     dic[i]=computer_selector[i]
  print("Guess the Characters")
  b=1
  while b<=len(computer_selector):
    c="-"
    lst.append(c)
    b+=1
  for i in lst:
    print(i)
  d=True
  con=0
  sr=''
  length=len(computer_selector)
  while len(sr)!=length and d==True:
    Input1=input("guess a character: ")
    if Input1 not in computer_selector:
      print(f"Try Again! You Have {a-1} turns are left")
      lst.clear()
      d=False
      b=True
    elif Input1 in computer_selector:
      for i,j in dic.items():
        if j==Input1:
          if lst[i]=="-":
             lst[i]=Input1
      for i in lst:
         if i==Input1:
           sr+=i
         print(i)
      if len(sr)==len(computer_selector):
        print("You Win")
        print(f"The Word is {computer_selector}")
        d=False
        b=False
  a-=1