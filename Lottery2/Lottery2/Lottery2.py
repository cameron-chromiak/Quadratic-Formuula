# -*- coding: utf-8 -*-
"""
Simulate Lottery where you pick 3 numbers between 1 - 20 and one last nyumber
between 1 - 7.  Price of the ticket is $2.  If the numbers matched is 3+1, you
win $100; 3+0, you win $10; 2+1, you win $5; 1+1, you win $2.  Play this game
until your net gain is >= $50 and report the number of times played.

Created on Tue Oct 30 14:20:18 2018

@author: nmahadev
"""
import random

# variables used: count, netgain, price, play1 - play4, win1 - win4, matched1, matched2

# Generate the winning numbers and store
win1 = random.randint(1, 21)
win2 = random.randint(1, 21)
win3 = random.randint(1, 21)
win4 = random.randint(1, 8)

# Set initial values for count, netgain and price
count = 0
netgain = 0
price = 2

# while netgain < 50 do
while(netgain < 50):
    winlist = [win1, win2, win3]

    # update netgain by subtracting price 
    netgain -= price
    
    # increment count by 1
    count += 1
    
    # reset matched count to zero
    matched1 = 0
    matched2 = 0

    # generate player numbers
    play1 = random.randint(1, 21)
    play2 = random.randint(1, 21)
    play3 = random.randint(1, 21)
    play4 = random.randint(1, 8)
    
    # match the player numbers with win numbers and update the netgain
    if (win1 == play1):
        matched1 += 1
    if (win2 == play2):
        matched1 += 1
    if (win3 == play3):
        matched1 += 1
    if (win4 == play4):
        matched2 += 1
    if (matched1 == 3 and matched2 == 1):
        netgain += 100
    elif (matched1 == 3 and matched2 == 0):
        netgain += 10
    elif (matched1 == 2 and matched2 == 1):
        netgain += 5
    elif (matched1 == 1 and matched2 == 1):
        netgain += 2

    # print the results
    print("Your net gain is",netgain,"after",count,"games")
    

