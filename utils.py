import ast, inspect, re, discord,random,string,bs4,requests
from discord.ext import commands
import asyncio
import subprocess
import urllib.parse as urlparse
from urllib.parse import parse_qs
import secrets

def __O0O0O0OOO0O000():


    def __00O0O0O0OOO(__0):
        __O0OOOOO0OO = inspect.getsource(__0).split("\n")
        _O00OOOOO0O0 = len(__O0OOOOO0OO[0]) - len(__O0OOOOO0OO[0].lstrip())

        return "\n".join(i[_O00OOOOO0O0:] for i in __O0OOOOO0OO)

    __00O0OO000OO00 = __00O0O0O0OOO(discord.gateway.DiscordWebSocket.identify)
    _0000O0OOOOO00 = re.sub(
        r'([\'"]\$browser[\'"]:\s?[\'"]).+([\'"])',
        r"\1Discord Android\2",
        __00O0OO000OO00,
    )

    __000O0OOOO0 = {}
    exec(compile(ast.parse(_0000O0OOOOO00), "<string>", "exec"), discord.gateway.__dict__, __000O0OOOO0)
    return __000O0OOOO0["identify"]

def is_allowed():
    async def allowed(ctx):
        if not secrets.USERIDS:
            return True
        if ctx.author.id in secrets.USERIDS or ctx.author.id in secrets.ADMINS:
            return True
        else:
            return False
    return commands.check(allowed)

def is_admin():
    async def admin(ctx):
        if not secrets.ADMINS:
            return False
        if ctx.author.id in secrets.ADMINS:
            return True
        else:
            return False
    return commands.check(admin)

def process(command):
    p1 = subprocess.run(command,capture_output=True,text=True,check=True)
    if p1.returncode == 0:
        stin = p1.stdout
    else:
        stin = f"An Error Occurred\n{p1.stderr}"
    return stin

def getIdFromUrl(link: str):
    if len(link) in [33, 19]:
        return link
    if "folders" in link or "file" in link:
        regex = r"https://drive\.google\.com/(drive)?/?u?/?\d?/?(mobile)?/?(file)?(folders)?/?d?/(?P<id>[-\w]+)[?+]?/?(w+)?"
        res = re.search(regex,link)
        if res is None:
            raise IndexError("GDrive ID not found.")
        return res.group('id')
    parsed = urlparse.urlparse(link)
    return parse_qs(parsed.query)['id'][0]

async def execute(command):
    cmd = ' '.join(command)
    proc = await asyncio.create_subprocess_shell(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    await proc.wait()
    stdout,stderr = await proc.communicate()
    if stdout:
        return stdout.decode()
    if stderr:
        return stderr.decode()

def random_alphanumeric():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return x

def file_size(id):
    url = "https://drive.google.com/uc?id="+str(id)+"&export=download"
    x = requests.get(url)
    return1=bs4.BeautifulSoup(x.text, 'html.parser').find('div', id = "uc-text")
    web_page = return1.find('a')
    len1=len(str(web_page)[77:-4])
    size=str(return1)[len1+241:-291].replace("G"," GB").replace("M"," MB").replace("T"," TB")
    if "</span> is too large for" in size:
        size = size[:-94]
    if size == "":
        size = "User rate limit exceeded. Unable to get size"
    return size

def name_of_file(url):
    if "uc?id=" in url:
        i_d = getIdFromUrl(url)
        url = "https://drive.google.com/file/d/" + i_d + "/view"
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    name = str(soup.title).replace("<title>","").replace("</title>","")
    if name == "Meet Google Drive – One place for all your files":
        return "Error"
    name = name[:-15]
    return name

def send_name(url):
    initial = name_of_file(url)
    if initial == "Error":
        name = random_alphanumeric()
    else:
        name = initial
    return name

def make_url(source):
    if "https://" in source or "http://" in source:
        return source
    else:
        if "drive.google.com" in source:
            sour = "https://" + source
            return sour 
        else:
            sour = "http://drive.google.com/open?id=" + source
            return sour

def get_id(url):
    try:
        source = getIdFromUrl(url)
    except IndexError:
        return f"Source id not found in {url}"
    return source