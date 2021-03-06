import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord.utils import get
import time
import os
import random
from itertools import cycle

chat_filter = []
bypass_list = []

Client = discord.Client()
client = commands.Bot(command_prefix = "%")
client.remove_command("help")
status = ['%help | EVO <3', '%help | Poly <3', '%help | Jack <3', '%help | TheDeibo <3', '%help | DeiiinaSea <3', 'Send Help!', 'Jack Beats Me']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)
        
@client.event
async def on_ready():
    print("bot is ready!")
        
@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "We do not allow that language here!")
                except discord.errors.NotFound:
                    return    
    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}, How Are You Today?'.format(message)
        await client.send_message(message.channel, msg)
        await client.process_commands(message)
    elif message.content.startswith('bye'):
        msg = 'GoodBye {0.author.mention}, Hope To See You Again Soon'.format(message)
        await client.send_message(message.channel, msg)
        await client.process_commands(message) 
    elif message.content.startswith('<@549399136802177026>'):
        msg = '{0.author.mention}, Why you tagging me '.format(message)
        await client.send_message(message.channel, msg) 
        await client.process_commands(message)
    elif message.content.startswith('<@540628244374749184'):
        msg = 'Jack is currently AFK he will respond soon!'
        await client.send_message(message.channel, msg)         
        await client.process_commands(message)       
    elif message.content.startswith(':zzz:'):
        if message.author == "Evo Bot#4846":
            emoji = get(client.get_all_emojis(),id='505440307085836288')
            await client.add_reaction(message, emoji)
            await client.process_commands(message)
        else:
            await client.process_commands(message)
    else:
        await client.process_commands(message)
        
@client.command(pass_context=True)
async def night(ctx):
       await client.delete_message(ctx.message)
       await client.say("**{}** Has gone to bed goodnight!".format(ctx.message.author))
  
@client.command(pass_context=True)
async def morning(ctx):
       await client.delete_message(ctx.message)
       await client.say("**{}** Has just woken up good morning!".format(ctx.message.author))

@client.command(pass_context=True)
async def nap(ctx):
       await client.delete_message(ctx.message)
       await client.say("**{}** Has gone to take a nap!".format(ctx.message.author))        
    
@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(title="EVO Server Infomation", color=0xff00ff)
    embed.add_field(name="IP", value="Coming Soon!", inline=False)
    embed.add_field(name="Forum", value="Coming Soon!", inline=False)
    embed.add_field(name="Discord", value="Coming Soon!", inline=False)
    embed.add_field(name="Vote", value="Coming Soon!", inline=False)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="EVO Bot Commands", description="Bot Prefix `%`", color=0xff00ff)
    embed.add_field(name="hello", value="Triggers when you say hello!", inline=False)
    embed.add_field(name="bye", value="Triggers when you say bye!", inline=False)
    embed.add_field(name="say", value="Makes the bot say something when using %say (admins only)!", inline=False)
    embed.add_field(name="info", value="Lists the EVO Server infomation!", inline=False)
    embed.add_field(name="night", value="Lets everyone know you are going to bed!", inline=False)
    embed.add_field(name="morning", value="Lets everyone know that you have woken up!", inline=False)
    embed.add_field(name="user", value="Lists some info on the user!", inline=False)
    embed.add_field(name="serverinfo", value="Lists the discord servers infomation!", inline=False)
    embed.add_field(name="kick", value="Kicks the member you tag!", inline=False)
    embed.add_field(name="ban", value="Bans the member you tag!", inline=False)
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def rules(ctx):
    embed = discord.Embed(title="------------------------------= Rules and Terms of Service =------------------------------", color=0xff00ff)
    embed.add_field(name="Rule 1", value="Please dont advertise other or non-partnered Discord/MC servers.", inline=False)
    embed.add_field(name="Rule 2", value="Be respectful and considerate towards staff and members. If you have any issues or concerns then a DM would be more appropriate.", inline=False)
    embed.add_field(name="Rule 3", value="Do not spam or use server BOTs incorrectly or with miss-use.", inline=False)
    embed.add_field(name="Rule 4", value="While in the server, do not hack or use Modified clients, as that will be an instant ban with no repeal, and smallest of any modified clients will not be tolerated.", inline=False)
    embed.add_field(name="Rule 5", value="Sexual content or inappropriate names will not be tolerated and will be warned, kicked, or banned.", inline=False)
    embed.add_field(name="Rule 6", value="For images and content posted on the website, please respect our copyright as well as regarding the Logo.", inline=False)
    embed.add_field(name="Rule 7", value="This server in no way reflects the status and reputation that of the public Evo Lobby Map. They are separate, any correlation if any is that I built both and both have the name Evo.", inline=False)
    embed.add_field(name="Rule 8", value="Also if you have any questions / comments / or concerns about anything DM staff, me of if you want to anonymously let us know, email us at support@evo.company.com", inline=False)
    await client.say(embed=embed)    
    
@client.command(pass_context=True)
async def user(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.message.author
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here is some info i could find on the user.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Nick", value=user.nick, inline=True)
    embed.add_field(name="Bot", value=user.bot, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role, inline=True)
    embed.add_field(name="Currently playing", value=user.game, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here is some info about the server.", color=0x00ff00)
    embed.set_author(name="Server Info!")
    embed.add_field(name="Server owner", value=ctx.message.server.owner, inline=True)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Channels", value=len(ctx.message.server.channels), inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members), inline=True)
    embed.add_field(name="Region", value=ctx.message.server.region, inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)  
    
@client.command(pass_context=True)
async def say(ctx, *, msg):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '540628244374749184':
        await client.delete_message(ctx.message)
        await client.send_message(ctx.message.channel, msg) 
    else:
        await client.say(":x: Error! You must have administrator permission!")     
        
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None):
    if user == None:
        embed = discord.Embed(name="", description="", color=0xff0000)
        embed.add_field(name="Usage", value="%kick <user>", inline=True)
        await client.say(embed=embed)
    else:
        if ctx.message.author.server_permissions.kick_members or ctx.message.author.server_permissions.administrator:
            await client.say("**{}** has been kicked out!".format(user.name))
            await client.kick(user)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You must have **Kick Members** or **Administrator** permission to use this command!", color=0xff0000)
            await client.say(embed=embed)

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None):
    if user == None:
        embed = discord.Embed(name="", description="", color=0xff0000)
        embed.add_field(name="Usage", value="%ban <user>", inline=True)
        await client.say(embed=embed)
    else:
        if ctx.message.author.server_permissions.ban_members or ctx.message.author.server_permissions.administrator:
            await client.say("**{}** has been banned from the server!".format(user.name))
            await client.ban(user)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You must have **Ban Members** or **Administrator** permission to use this command!", color=0xff0000)
            await client.say(embed=embed)
        
            
client.loop.create_task(change_status())
client.run(os.getenv('TOKEN'))
