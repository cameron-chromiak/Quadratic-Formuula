# -*- coding: utf-8 -*-
"""
Pick 3 numbers between 1-20 and one number between 1-7.  Ticket price is $2.
If you match 3+1, you win $100; 3+0, win $10; 2+1, win $5; 1+1, win $2. Simulate
the game by first generating the winning numbers.  Then play this game until your
net gain is >= $50 and display how many times you played.

Created on Tue Oct 30 09:51:14 2018

@author: nmahadev
"""
import random

# variables used: win1 - win4, play1 - play4, matched1, matched2, price, count, and netgain

# generate and store the winning numbers
win1 = random.randint(1, 11)
win2 = random.randint(1, 11)
win3 = random.randint(1, 11)
win4 = random.randint(1, 6)

# set initial values for count, netgain and price
count = 0
netgain = 0
price = 1

# while(netgain < 50) do
while(netgain < 50):

    # netgain -= price
    netgain -= price
    
    # count += 1
    count += 1
    
    # generate and store player numbers
    play1 = random.randint(1, 11)
    play2 = random.randint(1, 11)
    play3 = random.randint(1, 11)
    play4 = random.randint(1, 6)
    
    # check for a win and adjust netgain if needed
    matched1 = 0
    matched2 = 0
    if(win1 == play1):
        matched1 += 1
    if(win2 == play2):
        matched1 += 1
    if(win3 == play3):
        matched1 += 1
    if(win4 == play4):
        matched2 += 1
        
    if (matched1 == 3 and matched2 == 1):
        netgain += 100
    elif (matched1 == 3 and matched2 == 0):
        netgain += 10
    elif (matched1 == 2 and matched2 == 1):
        netgain += 5
    elif (matched1 == 1 and matched2 == 1):
        netgain += 2
    print("Your netgain is $", netgain, "after", count, "games.")
    
# print the results
print("Your netgain is $", netgain, "after", count, "games.")


