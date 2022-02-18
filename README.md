# Gclone Discord Utilities
## Features
1. **Clone**  - Clone a public/private google drive file/folder to your teamdrive.
2. **Mkdir**  - Make Directories directly from discord.
3. **Size**   - Calculate size of google drive files/folders from link.
4. **Move**   - Move files/folders from one location to other.
5. **sync**   - Sync source links to destination links.
6. **Delete** - Delete folders/files.
7. **Name**   - Find name of google drive folders/files from link.
## Prerequisites
Before you get started, you need [Python](https://www.python.org/) 3.7 or later to run this script. Below are some extra things you need to download / install too:

- **[Gclone](https://github.com/donwa/gclone)** - Run the shell / batch script if you are on Linux to install, or add the gclone.exe file to your system PATH variables if you are on Windows. Putting the script in the same directory as GClone in Windows will work as well. If you are on MacOS, download the Darwin build of GClone.
- **[AutoRClone](https://github.com/xyou365/autorclone) - (Service accounts folder)** - GClone requires service accounts. To generate and manage them, use AutoRClone. You can then configure GClone using the service accounts.

## Setup (Windows):
1. Download the [zip](https://codeload.github.com/jsmsj/Gclone-Discord-Utilities/zip/refs/heads/main) of the repo.
2. Run `pip install virtualenv` in your terminal.
3. Activate the virtual enviorment.
4. Run `pip install -r requirements.txt`
5. Create a discord bot account. Follow this [tutorial](https://discordpy.readthedocs.io/en/stable/discord.html), or you can refer to youtube.
6. Edit the [secrets.py](secrets.py) file.
7. Update the [rclone.conf](rclone.conf) file as per your need.
8. Open up your Terminal or Command Line and then `cd` into the directory of the Cloned GitHub Repo.
9. Run `python main.py` or `python3 main.py`. The output of the Terminal or Command Line should have no errors and show that everything is all ready!
---
**Enjoy using Gclone Discord Utilities Bot**
----
# Detailed Tutorial on Gclone and Service accounts setup

## How to create Service Accounts and add them to your teamdrive and setup gclone.
Follow [this tutorial](https://rentry.co/gcloneguide)

## How to set-up Gclone-Discord-Utilities bot 
_Coming soon ......_

---
