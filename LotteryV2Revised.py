# -*- coding: utf-8 -*-
"""
Pick 3 numbers between 1-20 and one number between 1-7.  Ticket price is $2.
If you match 3+1, you win $1000; 3+0, win $500; 2+1, win $100; 1+1, win $5. Simulate
the game by first generating the winning numbers.  Then play this game until your
net gain is >= $50 and display how many times you played.

In this version, matches are counted differently

Created on Tue Oct 30 09:51:14 2018

@author: nmahadev
"""
import random

# variables used: win1 - win4, play1 - play4, matched1, matched2, price, count, and netgain

# generate and store the winning numbers
win1 = random.randint(1, 21)
win2 = random.randint(1, 21)
win3 = random.randint(1, 21)
win4 = random.randint(1, 8)

# set initial values for count, netgain and price
count = 0
netgain = 0
price = 2

# while(-100 < netgain < 50) do
while(-1000 < netgain < 50):
    # Create a list of the first group of winning numbers
    winlist = [win1, win2, win3]
    print(winlist)

    # netgain -= price
    netgain -= price
    
    # count += 1
    count += 1
    
    # generate and store player numbers
    play1 = random.randint(1, 21)
    play2 = random.randint(1, 21)
    play3 = random.randint(1, 21)
    play4 = random.randint(1, 8)
    
    # check for a win and adjust netgain if needed
    matched1 = 0
    matched2 = 0
    for number in winlist:
      if (play1 == number):
        matched1 += 1
        winlist.remove(number)
        break
    for number in winlist:
      if (play2 == number):
        matched1 += 1
        winlist.remove(number)
        break
    for number in winlist:
      if (play3 == number):
        matched1 += 1
        winlist.remove(number)
        break
    if(win4 == play4):
        matched2 += 1
        
    if (matched1 >= 3 and matched2 == 1):
        netgain += 1000
    elif (matched1 >= 3 and matched2 == 0):
        netgain += 500
    elif (matched1 >= 2 and matched2 == 1):
        netgain += 100
    elif (matched1 >= 1 and matched2 == 1):
        netgain += 5
    print("Your netgain is $", netgain, "after", count, "games.")
    
# print the results
print("Your netgain is $", netgain, "after", count, "games.")


