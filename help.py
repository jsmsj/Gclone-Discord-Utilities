import discord
from discord.ext import commands
import secrets

class Help(commands.Cog,):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command = True)
    async def help(self,ctx):
        helpEmbed = discord.Embed(title = 'Help is here', color = discord.Color.green(), description = f"Use `{secrets.PREFIX}help <command>` for extended information")
        helpEmbed.add_field(name= "Gclone Integration", value = "`clone`, `mkdir`, `size`, `move`, `sync`, `deltefolder`, `deletefile`")
        helpEmbed.add_field(name= "Admin Only", value= "`add`, `remove`", inline=False )
        helpEmbed.add_field(name= "Utility (Anyone can use)", value= "`ping`, `size`, `name`, `info`", inline=False )
        helpEmbed.set_footer(text="Made with 💘 by jsmsj#5252 using pycord. Inspired from Rekulous' CloneCord.")
        await ctx.send(embed= helpEmbed)

    @help.command()
    async def clone(self,ctx):
        helpEmbed = discord.Embed(title = 'Clone', color = discord.Color.green(), description = "Clone a public or private google drive folder/file. Make sure your service accounts have access to the destination.\n[They also need to have access to the source incase you are cloning a private google drive file or folder]")
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}clone <source> [name] [destination]`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def ping(self,ctx):
        helpEmbed = discord.Embed(title = 'Ping', color = discord.Color.green(), description = "Used to test, if the bot is working and gives latency.")
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}ping`")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def mkdir(self,ctx):
        helpEmbed = discord.Embed(title = 'Make Directory', color = discord.Color.green(), description = "Make the path if it doesn't already exist.")
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}mkdir <name> [destination]`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def size(self,ctx):
        helpEmbed = discord.Embed(title = 'Size calculator', color = discord.Color.green(), description = "Returns the total size and number of objects in remote:path.")
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}size <source>`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def sync(self,ctx):
        helpEmbed = discord.Embed(title = 'Move', color = discord.Color.green(),
        description = "Sync the source to the destination, changing the destination\nonly.  Doesn't transfer unchanged files, testing by size and\nmodification time or MD5SUM.  Destination is updated to match\nsource, including deleting files if necessary."
        )
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}sync <source> <destination>`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def move(self,ctx):
        helpEmbed = discord.Embed(title = 'Sync', color = discord.Color.green(),
        description = "Moves the contents of the source directory to the destination\ndirectory. Gclone will error if the source and destination overlap and\nthe destination does not support a server side directory move operation."
        )
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}move <source> <destination>`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def deletefolder(self,ctx):
        helpEmbed = discord.Embed(title = 'Delete Folder', color = discord.Color.green(),
        description = "Remove the files in path given."
        )
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}deletefolder <source>`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def deletefile(self,ctx):
        helpEmbed = discord.Embed(title = 'Delete File', color = discord.Color.green(),
        description = "Remove a single file from remote.  Unlike `deletefolder` it cannot be used to\nremove a directory."
        )
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}deletefile <source>`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def name(self,ctx):
        helpEmbed = discord.Embed(title = 'Name', color = discord.Color.green(),
        description = "Get the name of file/folder from the given link. This is the name which will be used if you clone the file/folder"
        )
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}name <source>`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def add(self,ctx):
        helpEmbed = discord.Embed(title = 'Add', color = discord.Color.green(),
        description = "Add a member **temporarily** who can use the bot.\nFor permanentaly adding the member, update the secrets.py file."
        )
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}add <member>`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)
    
    @help.command()
    async def remove(self,ctx):
        helpEmbed = discord.Embed(title = 'Remove', color = discord.Color.green(),
        description = "Removes a member **temporarily** who can use the bot.\nFor permanentaly removing the member, update the secrets.py file."
        )
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}remove <member>`")
        helpEmbed.set_footer(text="Values enclosed in <> are REQUIRED. While values enclosed in [] are optional")
        await ctx.send(embed = helpEmbed)

    @help.command()
    async def info(self,ctx):
        helpEmbed = discord.Embed(title = 'About Me', color = discord.Color.green(), description = "To know more about me, run this command")
        helpEmbed.add_field(name="**Syntax**", value = f"`{secrets.PREFIX}info`")
        await ctx.send(embed = helpEmbed)

def setup(bot):
    bot.add_cog(Help(bot))
    print("Help cog is loaded")
