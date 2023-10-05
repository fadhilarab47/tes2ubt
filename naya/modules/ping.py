# @Rizzvbss | @Kenapanan | @SharingUserbot | Zaid-Userbot
# © @KynanSupport


import time
from datetime import datetime
from random import choice

from kymang import *
from kymang.raw.functions import Ping
from kymang.types import *

from . import *

TIME_DURATION_UNITS = (
    ("w", 60 * 60 * 24 * 7),
    ("d", 60 * 60 * 24),
    ("h", 60 * 60),
    ("m", 60),
    ("s", 1),
)

absen = [
    "**Hadir Sayang** 😳",
    "**Hadir Bro Kynan** 😁",
    "**Maaf ka habis nemenin ka Kynan** 🥺",
    "**Maaf ka habis disuruh Tuan Kynan** 🥺🙏🏻",
    "**Hadir Kynan Sayang** 😘",
    "**Hadir Kynan Akuuuuhhh** ☺️",
    "**Hadir Kynan brother Aku** 🥰",
    "**Sokap bet lu**",
    "**Apasi Bawel** 🥰",
]


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount}{unit}{"" if amount == 1 else ""}')
    return ":".join(parts)


@bots.on_message(filters.user(DEVS) & filters.command("Absen", "") & ~filters.me)
async def _(client, message):
    await message.reply(choice(absen))


@bots.on_message(filters.user(DEVS) & filters.command("Naya", "") & ~filters.me)
async def _(client, message):
    await message.reply_text("<b>Iya Naya Punya Nya Kynan🤩</b>")


@bots.on_message(filters.user(DEVS) & filters.command("Cping", "") & ~filters.me)
@bots.on_message(filters.command("ping", cmd) & filters.me)
async def _(client, message):
    start = time.time()
    current_time = datetime.now()
    await client.invoke(Ping(ping_id=randint(0, 2147483647)))
    delta_ping = round((time.time() - start) * 1000, 3)
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    emot_1 = await get_vars(client.me.id, "EMOJI_PING")
    emot_2 = await get_vars(client.me.id, "EMOJI_MENTION")
    emot_pong = emot_1 if emot_1 else "5269563867305879894"
    emot_mention = emot_2 if emot_2 else "6226371543065167427"
    if client.me.is_premium:
        _ping = f"""
<b><emoji id={emot_pong}>🏓</emoji>ᴘᴏɴɢ:</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b><emoji id={emot_mention}>👑</emoji>ᴍᴇɴᴛɪᴏɴ:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
"""
    else:
        _ping = f"""
<b>pong !!</b> `{delta_ping} ms`
<b>uptime:</b> `{uptime}`
<b>mention:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
"""
    await message.reply(_ping)


@app.on_callback_query(filters.regex("0_cls"))
async def now(_, cq):
    await cq.message.delete()
