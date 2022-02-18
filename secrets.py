"""
These are secret variables.
Add your bot token,prefix,allowed userids,
and default destination id/link for the bot
to upload files/folders.
"""

TOKEN = "" #your bot token

PREFIX = "" #add a space after the prefix

USERIDS = [] #can be left blank, if you want everyone to use the bot.

ADMINS = [] # enter user ids of admins here, these are the people who can add people or remove people from 'USERIDS' i.e. decide who can run the bot and who can not. MUST NOT REMAIN EMPTY

DESTINATION_ID = "" #This is the default destination id for bot to clone to. You can add a folder link here as well.

VERSION = "1.0.0" #This is the bot version. It is recommended that you do not change it.


from utils import getIdFromUrl
DEFAULT_DESTINATION_ID = getIdFromUrl(DESTINATION_ID)
