from art_higher_lower_game import logo
from art_higher_lower_game import vs
import random
print(logo)
from Data_higher_lower_game import data
a=random.choice(data)
name=''
description=''
country=''
follower_count=0
def checkfollowers(a):
    for i,j in a.items():
        if i=="follower_count":
            follower_count=j
            return follower_count
follower_count=checkfollowers(a)
current_score=0
def check(a):
    for i,j in a.items():
        if i=="name":
            name=j
        elif i=="description":
            description=j
        elif i=="country":
            country=j
        elif i=="follower_count":
            follower_count=j
    print(f"{name}, a {description}, from {country}.")
check(a)
print(vs)
b=random.choice(data)
follower_count1=0
follower_count1=checkfollowers(b)
check(b)
Input1=input("who has more followers? Type 'A' or 'B': ")
data.remove(a)
data.remove(b)
condition=True
while condition == True:
  if Input1=="A":
    if follower_count>follower_count1:
       current_score+=1
       print(logo)
       print(f"You're right! Current score: {current_score}")
       check(a)
       print(vs)
       follower_count1=0
       c=random.choice(data)
       follower_count1=checkfollowers(c)
       check(c)
       data.remove(c)
       Input1=input("who has more followers? Type 'A' or 'B': ")
       if Input1=="A" or Input1=="B":
        condition=True
    elif follower_count<follower_count1:
       print(f"Sorry, that's wrong. Final score: {current_score}")
       condition=False
  elif Input1=="B":
    if follower_count1>follower_count:
       current_score+=1
       print(logo)
       print(f"You're right! Current score: {current_score}")
       check(b)
       print(vs)
       d=random.choice(data)
       follower_count=0
       follower_count=checkfollowers(d)
       check(d)
       data.remove(d)
       Input1=input("who has more followers? Type 'A' or 'B': ")
       if Input1=="A" or Input1=="B":
        condition=True
    elif follower_count>follower_count1:
       print(f"Sorry, that's wrong. Final score: {current_score}")
       condition=False