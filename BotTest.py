import os
import random
import discord as discord
import requests
import random

#Template used: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    url = "https://api.datamuse.com/words?sp=" #Basic datamuse URL
    guess = ""

    if message.author == client.user:
        return

    if message.content.startswith("!hasThese:"): #Command from user
        guess = message.content[10:15] #Get the guessed letters
        more = message.content[15:]
        wordle = requests.get(url + guess)

        newWords = []
        containL = more.split()
        str = " "
        for i in wordle.json():
            if str not in i["word"]:
                newWords.append(i["word"])

        await message.channel.send("Have you tried " + newWords[random.randint(0, len(newWords) - 1)] + "?") #Output a random word from the list of suggested words
    elif message.content.startswith("!helpMe"):
        await message.channel.send("Commands: \nhasThese: Type in, without spaces, ?????. Fill in any letters that you know followed by any that are in the word")


client.run() #Bot token
