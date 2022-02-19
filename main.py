# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# ----------------------------------------------------------------------------------------------------------------------
# Gclone-Discord-Utilities Bot 1.0.0 by jsmsj.
# GClone made by Donwa on GitHub.
# Inspired from REKULOUS' CloneCord V6 Beta [https://github.com/Rekulous/CloneCord-Bot]
# Original Discord "GClone-Bot" by KushTheApplusser!
"""Imports"""
import discord, os
import traceback,sys
from discord.ext import commands,tasks
from itertools import cycle
import time
import secrets
from discord.ui import Button, View
from utils import __O0O0O0OOO0O000, is_allowed,process,execute,file_size,send_name,random_alphanumeric,make_url,is_admin,get_id


discord.gateway.DiscordWebSocket.identify = __O0O0O0OOO0O000()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(secrets.PREFIX))

bot.remove_command("help")
status = cycle([
    f'{secrets.PREFIX} ping',
    f'{secrets.PREFIX} help',
    'you clone some TBs',
    f'Version {secrets.VERSION}'
])
# # Setting `Playing ` status
# await bot.change_presence(activity=discord.Game(name="a game"))

# # Setting `Streaming ` status
# await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# # Setting `Listening ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# # Setting `Watching ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
@tasks.loop(seconds=60)
async def status_swap():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bot.user.id)
    print(process("gclone version"))
    print("---------------------------------------------------------------------")
    status_swap.start()

@bot.event
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        pass
    else:
        await ctx.send('An error occurred in {} command:\nContact the bot owner.'.format(ctx.command))
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)



@bot.command()
@is_allowed()
async def clone(ctx,source=None,name=None, destination=secrets.DEFAULT_DESTINATION_ID):
    if not source:
        return await ctx.send(f"Please tell the source link or id.\nFor correct usage run `{secrets.PREFIX}help clone`")
    start_time = time.time()
    source = make_url(source)
    destination = make_url(destination)
    destinatio = get_id(destination)
    if "Source id not found in" in destinatio:
        return await ctx.send(f"Id not found in {destination}")
    if name is None:
        try:
            name = await send_name(source)
        except:
            name = random_alphanumeric()
        name = await send_name(source)
    if name != None:
        d1 ='"'+"{"+ destinatio+"}"+"/"+ name + '"'
    else:
        d1 = "{" + destinatio + "}"
    sourc = get_id(source)
    if "Source id not found in" in sourc:
        return await ctx.send(f"Id not found in {source}")
    s1 = "{" + sourc + "}"
    cool = await ctx.send(
        "***Check the destination folder in 5 minutes if your clone is couple terabytes. If your clone is less than a terabyte, the clone will be complete within a couple of seconds!***"
    )
    cmd = ["gclone", "copy", f"GC:{s1}", f"GC:{d1}", "--transfers", "50", "-vP", "--stats-one-line", "--stats=15s", "--ignore-existing", "--drive-server-side-across-configs", "--drive-chunk-size", "128M", "--drive-acknowledge-abuse", "--drive-keep-revision-forever"]
    string = await execute(cmd)
    final = string[-1989::]
    fin = final.splitlines()[-1].split(",")
    
    logs =f"```ml\n{final}\n```"
    logs_2 =f"```ml\n Copied: {fin[0]}\n Completed: {fin[1]}\n{fin[-1]}\n Speed: {fin[2]}\n```"

    out = "<https://drive.google.com/drive/folders/{}>".format(destinatio)

    em = discord.Embed(title="**Cloning Complete**",description=logs_2,color=discord.Color.green())
    em.add_field(name="Link", value=out)
    em.add_field(name="Folder Name",value=name)
    end_time = time.time()
    taken_time = round((end_time-start_time)*1000)
    em.set_footer(text=f"Time taken: {taken_time}ms = {taken_time/1000}s")

    butt1 = Button(
    label="Show Details",
    style=discord.ButtonStyle.grey,
    emoji="⭐"
    )
    butt2 = Button(
        label="Get Public Link",
        style=discord.ButtonStyle.grey,
        emoji="🔗"
    )
    butt3 = Button(
        label="Gclone Command",
        style=discord.ButtonStyle.grey,
        emoji="🔗"
    )


    view = View()
    view.add_item(butt1)
    view.add_item(butt2)
    view.add_item(butt3)

    async def butt1call(interaction:discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you",ephemeral=True)
        else:
            butt1.disabled=True
            butt1.style = discord.ButtonStyle.success
            await interaction.response.edit_message(content=f"{ctx.author.mention}",embed=em,view=view)
            await interaction.followup.send(logs,ephemeral=True)
    
    async def butt2call(interaction:discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you",ephemeral=True)
        else:
            butt2.disabled=True
            butt2.style = discord.ButtonStyle.success
            await interaction.response.edit_message(content=f"{ctx.author.mention}",embed=em,view=view)
            com = ["gclone","link",f"GC:{d1}"]
            lik = await execute(com)
            em2 = discord.Embed(title="**Public Link**",description=lik,color=discord.Color.green())
            await cool.reply(embed=em2)
    
    async def butt3call(interaction:discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you",ephemeral=True)
        else:
            butt1.disabled=True
            butt1.style = discord.ButtonStyle.success
            await interaction.response.edit_message(content=f"{ctx.author.mention}",embed=em,view=view)
            await interaction.followup.send(f'gclone copy GC:"{d1}/{name}" "C:\\Users\\USERNAME\\Desktop\\{name} --progress"',ephemeral=True)
    
    butt1.callback = butt1call
    butt2.callback = butt2call
    butt3.callback = butt3call


    
    await cool.edit(content=f"{ctx.author.mention}",embed=em,view=view)


@bot.command()
async def ping(ctx):
    start_time = time.time()
    message = await ctx.send("Pinging...")
    end_time = time.time()

    await message.edit(content=f":ping_pong:    *Pong!*    **`{round(bot.latency * 1000)}ms`**    :ping_pong:\n:ping_pong:    **API Ping:** **`{round((end_time - start_time) * 1000)}ms`**  :ping_pong:")

@bot.command()
@is_allowed()
async def mkdir(ctx,name=None, source=secrets.DEFAULT_DESTINATION_ID):
    if not name:
        return await ctx.send(f"Directory name not given.\nFor correct usage run `{secrets.PREFIX}help mkdir`")
    start_time = time.time()
    source = make_url(source)
    sourc = get_id(source)
    if "Source id not found in" in sourc:
        return await ctx.send(f"Id not found in {source}")
    s1 = "{" + sourc + "}"
    msg = await ctx.send(
        "***Creating directory...***"
    )
    cmd =["gclone", "mkdir", f'GC:"{s1}{name}"']
    await execute(cmd)
    em = discord.Embed(title="**Directory created**",color=discord.Color.green())
    em.add_field(name="Link", value="<https://drive.google.com/drive/folders/{}>".format(sourc))
    end_time = time.time()
    taken_time = round((end_time-start_time)*1000)
    em.set_footer(text=f"Time taken: {taken_time}ms = {taken_time/1000}s")
    await msg.edit(content=ctx.author.mention,embed=em)


@bot.command()
async def size(ctx,source=None):
    if not source:
        return await ctx.send(f"Source not given.\nFor correct usage run `{secrets.PREFIX}help size`")
    start_time = time.time()
    soure = make_url(source)
    sour = get_id(soure)
    if "Source id not found in" in sour:
        return await ctx.send(f"Id not found in {source}")
    s1 = "{" + sour + "}"
    msg = await ctx.send("***Caclulating size ...***")
    cmd = ["gclone", "size",f"GC:{s1}","--fast-list"]
    out = await execute(cmd)

    testing = out.splitlines()
    if testing[-1] == "Total size: 0 Bytes (0 Bytes)" and testing[0] == "Total objects: 0":
        try:
            out = await file_size(sour)
        except AttributeError:
            pass
    em = discord.Embed(title="**Size Calculated**",description=f"```py\n{out}\n```",color=discord.Color.green())
    end_time = time.time()
    taken_time = round((end_time-start_time)*1000)
    em.set_footer(text=f"Time taken: {taken_time}ms = {taken_time/1000}s")

    await msg.edit(content=ctx.author.mention,embed=em)

@bot.command()
@is_allowed()
async def move(ctx, source=None, destination=None):
    if not source:
        return await ctx.send(f"Source not given.\nFor correct usage run `{secrets.PREFIX}help move`")
    if not destination:
        return await ctx.send(f"Destination not given.\nFor correct usage run `{secrets.PREFIX}help move`")
    start_time = time.time()
    source,destination = make_url(source),make_url(destination)
    sourc,destinatio = get_id(source),get_id(destination)
    if "Source id not found in" in sourc:
        return await ctx.send(f"Id not found in {source}")
    if "Source id not found in" in destinatio:
        return await ctx.send(f"Id not found in {destination}")
    s1 = "{" + sourc + "}"
    d1 = "{" + destinatio + "}"
    msg = await ctx.send(
        "***Check the destination folder in 5 minutes if your transfer is couple terabytes. If your transfer is less than a terabyte, the clone will be complete within a couple of seconds!***"
    )
    cmd=["gclone", "move", f"GC:{s1}", f"GC:{d1}", "--transfers", "50", "--tpslimit-burst", "50", "--checkers", "10", "-vP", "--stats-one-line", "--stats=15s", "--ignore-existing", "--drive-server-side-across-configs", "--drive-chunk-size", "128M", "--drive-acknowledge-abuse", "--drive-keep-revision-forever", "--fast-list"]
    out = await execute(cmd)
    final = out[-1989::]
    logs =f"```ml\n{final}\n```"
    em = discord.Embed(title="**File Transfers Completed**",color=discord.Color.green())
    em.add_field(name="Link",value="https://drive.google.com/drive/folders/{}".format(destinatio))
    end_time = time.time()
    taken_time = round((end_time-start_time)*1000)
    em.set_footer(text=f"Time taken: {taken_time}ms = {taken_time/1000}s")

    butt1 = Button(
    label="Show Details",
    style=discord.ButtonStyle.grey,
    emoji="⭐"
    )
    butt2 = Button(
        label="Get Public Link",
        style=discord.ButtonStyle.grey,
        emoji="🔗"
    )


    view = View()
    view.add_item(butt1)
    view.add_item(butt2)

    async def butt1call(interaction:discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you",ephemeral=True)
        else:
            butt1.disabled=True
            butt1.style = discord.ButtonStyle.success
            await interaction.response.edit_message(content=f"{ctx.author.mention}",embed=em,view=view)
            await interaction.followup.send(logs,ephemeral=True)
    
    async def butt2call(interaction:discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you",ephemeral=True)
        else:
            butt2.disabled=True
            butt2.style = discord.ButtonStyle.success
            await interaction.response.edit_message(content=f"{ctx.author.mention}",embed=em,view=view)
            com = ["gclone","link",f"GC:{d1}"]
            lik = await execute(com)
            em2 = discord.Embed(title="**Public Link**",description=lik,color=discord.Color.green())
            await msg.reply(embed=em2)
    
    butt1.callback = butt1call
    butt2.callback = butt2call

    await msg.edit(content=ctx.author.mention,embed=em,view=view)



@bot.command()
@is_allowed()
async def sync(ctx, source=None, destination=None):
    if not source:
        return await ctx.send(f"Source not given.\nFor correct usage run `{secrets.PREFIX}help sync`")
    if not destination:
        return await ctx.send(f"Destination not given.\nFor correct usage run `{secrets.PREFIX}help sync`")
    start_time = time.time()
    source,destination = make_url(source),make_url(destination)
    sourc,destinatio = get_id(source),get_id(destination)
    if "Source id not found in" in sourc:
        return await ctx.send(f"Id not found in {source}")
    if "Source id not found in" in destinatio:
        return await ctx.send(f"Id not found in {destination}")
    s1 = "{" + source + "}"
    d1 = "{" + destinatio + "}"
    msg = await ctx.send(
        "***GcloneBot is syncing... it should be done syncing in a couple of minutes!***"
    )
    cmd = ["gclone", "sync", f"GC:{s1}", f"GC:{d1}", "--transfers", "50", "--tpslimit-burst", "50", "--checkers", "10", "-vP", "--stats-one-line", "--stats=15s", "--drive-server-side-across-configs", "--drive-chunk-size", "128M", "--drive-acknowledge-abuse", "--drive-keep-revision-forever", "--fast-list"]
    out = await execute(cmd)
    final = out[-1989::]
    logs =f"```ml\n{final}\n```"
    em = discord.Embed(title="**Sync Completed**",color=discord.Color.green())
    em.add_field(name="Link",value="https://drive.google.com/drive/folders/{}".format(destinatio))
    end_time = time.time()
    taken_time = round((end_time-start_time)*1000)
    em.set_footer(text=f"Time taken: {taken_time}ms = {taken_time/1000}s")

    butt1 = Button(
    label="Show Details",
    style=discord.ButtonStyle.grey,
    emoji="⭐"
    )
    butt2 = Button(
        label="Get Public Link",
        style=discord.ButtonStyle.grey,
        emoji="🔗"
    )


    view = View()
    view.add_item(butt1)
    view.add_item(butt2)

    async def butt1call(interaction:discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you",ephemeral=True)
        else:
            butt1.disabled=True
            butt1.style = discord.ButtonStyle.success
            await interaction.response.edit_message(content=f"{ctx.author.mention}",embed=em,view=view)
            await interaction.followup.send(logs,ephemeral=True)
    
    async def butt2call(interaction:discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you",ephemeral=True)
        else:
            butt2.disabled=True
            butt2.style = discord.ButtonStyle.success
            await interaction.response.edit_message(content=f"{ctx.author.mention}",embed=em,view=view)
            com = ["gclone","link",f"GC:{d1}"]
            lik = await execute(com)
            em2 = discord.Embed(title="**Public Link**",description=lik,color=discord.Color.green())
            await msg.reply(embed=em2)
    
    butt1.callback = butt1call
    butt2.callback = butt2call

    await msg.edit(content = ctx.author.mention, embed=em,view=view)



@bot.command()
@is_allowed()
async def deletefolder(ctx, source=None):
    if not source:
        return await ctx.send(f"Source not given.\nFor correct usage run `{secrets.PREFIX}help deletefolder`")
    start_time = time.time()
    souce = make_url(source)
    sourc = get_id(souce)
    if "Source id not found in" in sourc:
        return await ctx.send(f"Id not found in {source}")
    s1 = "{" + sourc + "}"
    msg = await ctx.send(
        "*GcloneBot is emptying the directory... it should be done in around 5 minutes if your directory is big! You **cannot** recover these from the **trashcan***"
    )
    cmd=["gclone", "delete", f"GC:{s1}", "-vP","--stats-one-line", "--stats=15s", "--fast-list"]
    out = await execute(cmd)
    final = out[-1989::]
    logs =f"```ml\n{final}\n```"
    em = discord.Embed(title="**Directory Emptied**",color=discord.Color.green())
    em.add_field(name="Link",value="https://drive.google.com/drive/folders/{}".format(sourc))
    end_time = time.time()
    taken_time = round((end_time-start_time)*1000)
    em.set_footer(text=f"Time taken: {taken_time}ms = {taken_time/1000}s")

    butt1 = Button(
    label="Show Details",
    style=discord.ButtonStyle.grey,
    emoji="⭐"
    )


    view = View()
    view.add_item(butt1)

    async def butt1call(interaction:discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you",ephemeral=True)
        else:
            butt1.disabled=True
            butt1.style = discord.ButtonStyle.success
            await interaction.response.edit_message(content=f"{ctx.author.mention}",embed=em,view=view)
            await interaction.followup.send(logs,ephemeral=True)
    
    
    butt1.callback = butt1call

    await msg.edit(content = ctx.author.mention, embed=em,view=view)



@bot.command()
@is_allowed()
async def deletefile(ctx, source=None):
    if not source:
        return await ctx.send(f"Source not given.\nFor correct usage run `{secrets.PREFIX}help deletefile`")
    start_time = time.time()
    source = make_url(source)
    sourc = get_id(source)
    if "Source id not found in" in sourc:
        return await ctx.send(f"Id not found in {source}")
    s1 = "{" + sourc + "}"
    msg = await ctx.send(
        "*GcloneBot is deleting the file... it should be done in around 5 minutes if your file is big!* **If you are worried about losing your deleted file forever, don't worry! You can recover stuff from your trash can!**"
    )
    cmd=["gclone", "deletefile", f"GC:{s1}", "-vP", "--drive-trashed-only","--stats-one-line", "--stats=15s", "--fast-list"]
    out = await execute(cmd)
    final = out[-1989::]
    logs =f"```ml\n{final}\n```"
    em = discord.Embed(title="**File deleted**",color=discord.Color.green())
    end_time = time.time()
    taken_time = round((end_time-start_time)*1000)
    em.set_footer(text=f"Time taken: {taken_time}ms = {taken_time/1000}s")

    butt1 = Button(
    label="Show Details",
    style=discord.ButtonStyle.grey,
    emoji="⭐"
    )


    view = View()
    view.add_item(butt1)

    async def butt1call(interaction:discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you",ephemeral=True)
        else:
            butt1.disabled=True
            butt1.style = discord.ButtonStyle.success
            await interaction.response.edit_message(content=f"{ctx.author.mention}",embed=em,view=view)
            await interaction.followup.send(logs,ephemeral=True)
    
    
    butt1.callback = butt1call

    await msg.edit(content = ctx.author.mention, embed=em,view=view)

@bot.command()
async def name(ctx,source=None):
    if not source:
        return await ctx.send(f"Source not given.\nFor correct usage run `{secrets.PREFIX}help size`")
    start_time = time.time()
    soure = make_url(source)
    sour = get_id(soure)
    if "Source id not found in" in sour:
        return await ctx.send(f"Id not found in {source}")
    msg = await ctx.send("***Finding Name ...***")
    nam = await send_name(soure)
    if nam == "":
        nam = "Cannot get name\nThe given file/folder is private."
    em = discord.Embed(title="**Name determined**",description=f"```py\n{nam}\n```",color=discord.Color.green())
    end_time = time.time()
    taken_time = round((end_time-start_time)*1000)
    em.set_footer(text=f"Time taken: {taken_time}ms = {taken_time/1000}s")

    await msg.edit(content=ctx.author.mention,embed=em)


@bot.command()
@is_admin()
async def add(ctx,mem:discord.Member=None):
    if not mem:
        return await ctx.send(f"Member not given.\nFor correct usage run `{secrets.PREFIX}help")
    secrets.USERIDS.append(mem.id)
    em = discord.Embed(title="**Added member**",description=f"{mem.mention} can now **temporarily** use the bot.",color=discord.Color.green())
    em.set_footer(text="For adding a permanent member, update the secrets.py file yourself.")
    await ctx.send(embed=em)

@bot.command()
@is_admin()
async def remove(ctx,mem:discord.Member=None):
    if not mem:
        return await ctx.send(f"Member not given.\nFor correct usage run `{secrets.PREFIX}help")
    secrets.USERIDS.remove(mem.id)
    em = discord.Embed(title="**Removed member**",description=f"{mem.mention} cannot use the bot anymore.",color=discord.Color.green())
    await ctx.send(embed=em)

@bot.command()
async def info(ctx):
    em = discord.Embed(title="Who am I ?",description="I am Gclone Discord Utility Bot. My main goal is to help you clone some TBs from discord. I use [gclone](https://github.com/donwa/gclone) to make this possible. It is recommended to use service accounts to bypass the 750GB upload limit per day.\n**A tutorial can be found in the bot's repository on github.**",color=discord.Color.green())
    em.add_field(name="Made By",value="jsmsj#5252\n(DMs Open for recommendations.)")
    em.add_field(name="Version",value=secrets.VERSION)
    em.add_field(name="Bot Repository",value="[Gclone Discord Utilities](https://github.com/jsmsj/Gclone-Discord-Utilities)")
    em.add_field(name="All Commands",value=f"`{secrets.PREFIX}help`")
    em.add_field(name="Inspired by",value="[Rekulous' CloneCord](https://github.com/Rekulous/CloneCord-Bot)")
    em.add_field(name="Bot Language",value="Python (Pycord)")

    await ctx.send(embed=em)


bot.load_extension('help')
bot.run(secrets.TOKEN)
