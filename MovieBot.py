import discord
from discord.ext import commands

import random

# Helper functions

def OpenFile(newMovie):
    
    fileName = "movieList.txt"
    file = open(fileName, "r")
    
    # Add each file line to a list
    
    movieList = []
    
    for line in file:
        movieList.append(line.strip())
       
    file.close()

    # Append new movie to end of file
    file = open(fileName, "a")
    file.write(newMovie + "\n")
    file.close()
    
    # Append new movie to end of list
    movieList.append(newMovie)

    return movieList

def DeleteMovie(movieTitle):
    
    fileName = "movieList.txt"
    file = open(fileName, "r")
    
    # Add each file line to a list
    
    movieList = []
    
    for line in file:
        if(line.strip() != movieTitle):
            # Add the movie to the list if its not the movie to be deleted
            movieList.append(line.strip())

    file.close()
    
    file = open(fileName, "w")
    
    for movie in movieList:
        file.write(movie + "\n")
        
    return movieList

def FormatList(list):
    
    formattedList = ""
    
    for line in list:
        if(line != ''):
            # Add line the string
            formattedList += "- " + line + "\n"
            
    return formattedList

def ViewMovies():
    
    fileName = "movieList.txt"
    file = open(fileName, "r")
    
    # Add each file line to a list
    
    movieList = []
    
    for line in file:
        movieList.append(line.strip())
       
    file.close()
    
    return movieList

def PickRandomMovie():
    
    fileName = "movieList.txt"
    file = open(fileName, "r")
    
    # Add each file line to a list
    
    movieList = []
    counter = 0
    
    for line in file:
        counter = counter + 1
        movieList.append(line.strip())
       
    file.close()
    
    randMovie = movieList[random.randint(0, counter - 1)]
    
    return randMovie
    
# End of helper functions    

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready!')
    await client.change_presence(activity=discord.Game(name="MovieBot .movieHelp"))
    
@client.command()
async def addMovie(ctx, *, movieTitle):
    if(ctx.message.channel.id == 829860701895131147):
        list = OpenFile(movieTitle)
        list = FormatList(list)
        await ctx.send("The movie has been added: " + movieTitle + "\n" + list)
        
@client.command()
async def deleteMovie(ctx, *, movieTitle):
    if(ctx.message.channel.id == 829860701895131147):
        list = DeleteMovie(movieTitle)
        list = FormatList(list)
        await ctx.send("The movie has been deleted: " + movieTitle + "\n" + list)
        
@client.command()
async def viewMovies(ctx):
    if(ctx.message.channel.id == 829860701895131147):
        list = ViewMovies()
        list = FormatList(list)
        await ctx.send("The current list of movies is:\n" + list)        
        
@client.command()
async def movieHelp(ctx):
    if(ctx.message.channel.id == 829860701895131147):
        await ctx.send("Commands:\n.addMovie - Adds a movie to the list\n.deleteMovie - " +
                       "Deletes an existing movie from the list\n.viewMovies - Displays " +
                       "a list of all the movies\n.randomMovie - Displays a random movie from the list")
        
@client.command()
async def randomMovie(ctx):
    if(ctx.message.channel.id == 829860701895131147):
        randMovie = PickRandomMovie()
        await ctx.send(randMovie)  
    
client.run('ODI5ODU2MDY5NTU5MTI0MDAw.YG-NsA.JdJf9toDOqLRLC2KzQCszfsNhkI')

