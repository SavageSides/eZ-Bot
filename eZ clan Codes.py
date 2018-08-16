#Made by ✦𝕊𝕒𝕍𝕒𝔾𝕖✦;_;#2112
#Hopefully they will like it

import discord
from discord.ext import commands
import random

TOKEN = 'NDc5NDEzNTc2ODY0NjI4NzQy.DlY4oQ.vT5Ofkkwd10VzjPDphhOMfN8bQ4'

client = commands.Bot(command_prefix='ez!')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Working on the bot Right Now!'))
    print('Logged In as')
    print(client.user.name)
    print(client.user.id)
    print('The bot is connected to discord and ready to work!')

@client.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, user: discord.Member):
    await client.say("***User has been kicked.*** :white_check_mark:")
    await client.kick(user)

@client.command(pass_context=True)
@commands.has_role("Admin")
async def ban(ctx, user: discord.Member):
    await client.say("***User has been banned.*** :white_check_mark:")
    await client.ban(user)

@client.command(pass_context=True)
@commands.has_role("Admin")
async def purge(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('***Messages Deleted!*** :white_check_mark:')




#Help and Displays

@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        colour = discord.Colour.orange()

    )

    embed.set_author(name='eZ Help Center')
    embed.add_field(name='Mod Help', value='Returns a command that sends a message to your Direct Messages telling you all your commands! P.S Only Staff Can use this command', inline=False)
    embed.add_field(name='userinfo', value='Sends the user a message in the channel, about the person they wanted to know about!', inline=True)
    
    await client.say(embed=embed)

@client.command(pass_context=True)
@commands.has_role("Admin")
async def modhelp(ctx):
    author = ctx.message.author


    embed = discord.Embed(
        colour = discord.Colour.dark_orange()

    )

    embed.set_author(name='eZ Mod Help Center')
    embed.add_field(name='ez!Kick', value='This command is for kicking people who dont behave :smile:', inline=False)
    embed.add_field(name='ez!ban', value='This command is for when someone behaves so bad you have to punish them to not come back!', inline=True)
    embed.add_field(name='ez!purge', value='This command will delete the messages. Tell it a number between 1 and 100 and it will purge it. P.S Use carefully', inline=True)

    await client.say("**Bot has sent you a message!**")

    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="eZ Clan info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)





client.run(TOKEN)
