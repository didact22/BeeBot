#Bee Bot Base File

import discord
import random
import requests
import discord 
import valve 
import valve.source
import valve.source.a2s
import valve.source.master_server
from discord.ext import commands
from discord.ext.commands import Bot
import time
import datetime
from datetime import datetime
import asyncio
import chalk
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='.')
dClient = discord.Client
msgQ = [] #stores a tuple (player name + dino, time)

pDict = {"319090800715628544": ["EST",["Dodo","Giga"],True],
         "Upton":("CST",[])
                  }# stores player, time zone, dinos requested

@bot.event 
async def on_ready():
    print("Ready when you are Dave")
    print("I am running on " + bot.user.name)
    print("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! ")

@bot.command(pass_context=True)
async def msgUser(ctx,dino, strabH, strabM):#can use this function to post the dino name, absolute time to pop, and times by time zone that dinos are popping
    abH,abM = int(strabH), int(strabM) #convert string input to ints for operations
    now = datetime.now()
    gmt = time.gmtime()
    gmtHour = gmt[3]
    gmtMin = gmt[4]
    hr = now.hour
    min = now.minute
    print (now)
    print (hr)
    print (min)
    print (gmt)
    print (gmtHour)
    print (gmtMin)
    pstH = (gmtHour - 8) % 24 #these are current times in hours!
    mstH = (gmtHour - 7) % 24 #these are current times in hours!
    cstH = (gmtHour - 6) % 24 #these are current times in hours!
    estH = (gmtHour - 5) % 24 #these are current times in hours!
    cetH = (gmtHour + 1) % 24 #these are current times in hours!
    kstH = (gmtHour + 9) % 24 #these are current times in hours!
    print ("PST: " + str(pstH) + "\n" + "EST: " + str(estH))
    gpM = abM + min
    if (abM + min > 60):
        abH += 1
        gpM = (abM + min) % 60
    gpH = (abH + gmtHour) % 24 
    pacPH = (abH + pstH) % 24
    mtnPH = (abH + mstH) % 24
    cenPH = (abH + cstH) % 24
    eastPH = (abH + estH) % 24
    eurPH = (abH + cetH) % 24
    korPH = (abH + kstH) % 24
    await bot.say(" The input I got was " + dino + " " + strabH + " "+ strabM + " " + numDino) # the inputs seem to be strings
    await bot.say(dino + " Due in " + strabH + " Hours and " + strabM + " Minutes")
    await bot.say("PST- " + str(pacPH) + ":" + str(gpM))
    await bot.say("MST- " + str(mtnPH) + ":" + str(gpM))
    await bot.say("CST- " + str(cenPH) + ":" + str(gpM))
    await bot.say("EST- " + str(eastPH) + ":" + str(gpM))
    await bot.say("CET- " + str(eurPH) + ":" + str(gpM))
    await bot.say("KST- " + str(korPH) + ":" + str(gpM))
    await bot.say("GMT- " + str(gpH) + ":" + str(gpM))
    await bot.say("@here")
    #TESTING    userDM = await bot.get_user_info(319090800715628544) #testing
    #TESTING    print(userDM)
    #TESTING    await bot.send_message(userDM, dino + " will be ready in " + strabH + " Hours and " + strabM + " Minutes" )
    for player in pDict:#for every player ID in the dictionary
        for babyType in pDict[player][1]: #for every dino in the players dino list
            if dino == babyType:
                userDM = await bot.get_user_info(int(player))#can use the UserDM to send messages to a specific user
                await bot.send_message(userDM, dino + " Due in " + strabH + " Hours and " + strabM + " Minutes")
                if pDict[player][0] == "PST":
                   await bot.send_message(userDM,"PST- " + str(pacPH) + ":" + str(gpM))
                elif pDict[player][0] == "MST":
                   await bot.send_message(userDM,"MST- " + str(mtnPH) + ":" + str(gpM))
                elif pDict[player][0] == "CST":
                    await bot.send_message(userDM,"CST- " + str(cenPH) + ":" + str(gpM))
                elif pDict[player][0] == "EST":
                   await bot.send_message(userDM,"EST- " + str(eastPH) + ":" + str(gpM))
                elif pDict[player][0] == "CET":
                    await bot.send_message(userDM,"CET- " + str(eurPH) + ":" + str(gpM))
                elif pDict[player][0] == "KST":
                    await bot.send_message(userDM,"KST- " + str(korPH) + ":" + str(gpM))
                elif pDict[player][0] == "GMT":
                   await bot.send_message(userDM,"GMT- " + str(gpH) + ":" + str(gpM))

    #for player in pDict:# if dino is in someones request list send them a message that includes the absolute time and their timezone.
     #   for din in pDict[player][1]: # looks in the dino list for each player
      #      if din == dino:# if the dino matches, have the bot DM the player with the info(tz, time to pop) and add a 20 min reminder
       #         playerTZ = pDict[player][0]
                #discord.utils.find(lambda m: m.id == int(player),dClient.send_message )
        #        userDM = bot.get_user_info(int(player))
                #await userDM.send(dino + " will be ready in " + strabH + " Hours and " + strabM + " Minutes")
         #       bot.send_message(userDM, dino + " will be ready in " + strabH + " Hours and " + strabM + " Minutes" )
                


                #MESSAGE THE PLAYER that the dinos will be ready in the absolute time with their timezone displayed.
                #also enqueue the player to receive a 20 min prior notice
    
@bot.command(pass_context=True)
async def stopNotif(ctx, playerName): # does not send a msg to a player if it is posted (set the 3rd dStruct in the dictionary to false) ,do we need True/False Flag in pDict? Probably.
    for player in pDict:#works when tested against Didact's ID and list
        if player == playerName:
            print(player)
            pDict[player][2] = False
            print(pDict[player][2])

@bot.command(pass_context=True)
async def startNotif(ctx, playerName):# begins notifications for a player, sets the true/false flag to true. Can put all to be notified for all dinos
    for player in pDict:#works when tested against Didact's ID and list
        if player == playerName:
            print(player)
            pDict[player][2] = True
            print(pDict[player][2])

@bot.command(pass_context=True)
async def addDino(ctx, playerName, dino): #adds a dino in a specific players list so that they are notified of that dino popping
    for player in pDict:#works when tested against Didact's ID and list
        if player == playerName:
            print(pDict[player][1])
            pDict[player][1].append(dino)
            print(pDict[player][1])

@bot.command(pass_context=True)
async def changeTimezone(ctx, playerName, tz):#overwrites an existing timezone for a specific player
    for player in pDict:#works when tested against Didact's ID and list
        if player == playerName:
            print(pDict[player][0])
            pDict[player][0] = tz
            print(pDict[player][0])

@bot.command(pass_context=True)
async def addPlayer(ctx, playerName, tz):#creates a new entry in the dictionary for a new player
    pDict[str(playerName)] = [tz,[],True]
    print (pDict)

@bot.command(pass_context=True)
async def showList(ctx):
    print(pDict)







bot.run("NTAxOTU1NzQ4NjA0MTQ5Nzcw.DrFQyg.5XwuartdG-jMwT0p2Apspp6NQqc")
