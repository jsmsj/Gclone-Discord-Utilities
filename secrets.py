"""
These are secret variables.
Add your bot token,prefix,allowed userids,
and default destination id/link for the bot
to upload files/folders.
"""
import dotenv,os
dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

PREFIX = os.getenv("PREFIX")

USERIDS = []
temp = os.getenv("USERIDS").split(',')
if temp[0] != "none":
    for user in temp:
        USERIDS.append(int(user))

ADMINS = []
tempp = os.getenv("ADMINS").split(',')
for admin in tempp:
    ADMINS.append(int(admin))


DESTINATION_ID = os.getenv("DESTINATION_ID") 

VERSION = "1.5.0" #This is the bot version. It is recommended that you do not change it.


from utils import getIdFromUrl
DEFAULT_DESTINATION_ID = getIdFromUrl(DESTINATION_ID)
