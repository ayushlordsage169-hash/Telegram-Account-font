from telethon import TelegramClient, events
import json
import os
from threading import Thread
from flask import Flask

# ========= WEB SERVER =========
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

Thread(target=run_web).start()

# ========= ENV VARIABLES =========
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient('session', api_id, api_hash)

# ========= MEMORY =========
try:
    with open("font.json", "r") as f:
        font_mode = json.load(f)
except:
    font_mode = {"status": False, "style": 1}

def save():
    with open("font.json", "w") as f:
        json.dump(font_mode, f)

# ========= FONT =========
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fonts = {
1: str.maketrans(lower+upper,
                 "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀꜱᴛᴜᴠᴡxʏᴢ"+
                 "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀꜱᴛᴜᴠᴡxʏᴢ"),

2: str.maketrans(lower+upper,
                 "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"+
                 "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩"),

3: str.maketrans(lower+upper,
                 "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"+
                 "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"),

4: str.maketrans(lower+upper,
                 "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"+
                 "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅"),

5: str.maketrans(lower+upper,
                 "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"+
                 "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"),

6: str.maketrans(lower+upper,
                 "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"+
                 "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"),

7: str.maketrans(lower+upper,
                 "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"+
                 "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"),

8: str.maketrans(lower+upper,
                 "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"+
                 "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"),
}

def upside(text):
    table = str.maketrans(lower, "ɐqɔpǝɟɓɥᴉɾʞlɯuodbɹsʇnʌʍxʎz")
    return text.translate(table)[::-1]

@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    msg = event.raw_text

    if msg.startswith("/font_list"):
        sample = "Har har Mahadev 🙏"
        previews = {
            1: sample.translate(fonts[1]),
            2: sample.translate(fonts[2]),
            3: sample.translate(fonts[3]),
            4: sample.translate(fonts[4]),
            5: sample.translate(fonts[5]),
            6: sample.translate(fonts[6]),
            7: sample.translate(fonts[7]),
            8: sample.translate(fonts[8]),
            9: sample[::-1],
            10: upside(sample),
        }

        text = "🎨 Font List:\n\n"
        for i in range(1, 11):
            text += f"{i} → {previews[i]}\n\n"

        await event.edit(text)
        return

    if msg.startswith("/font_on"):
        try:
            num = int(msg.split()[1])
            if num < 1 or num > 10:
                raise ValueError

            font_mode["status"] = True
            font_mode["style"] = num
            save()
            await event.edit(f"Font {num} ON")
        except:
            await event.edit("Use: /font_on 1-10")

    elif msg.startswith("/font_off"):
        font_mode["status"] = False
        save()
        await event.edit("Font OFF")

    elif font_mode["status"] and not msg.startswith("/"):
        if font_mode["style"] in fonts:
            new = msg.translate(fonts[font_mode["style"]])
        elif font_mode["style"] == 9:
            new = msg[::-1]
        elif font_mode["style"] == 10:
            new = upside(msg)
        else:
            return

        if new != msg:
            await event.edit(new)

client.start()
client.run_until_disconnected()
