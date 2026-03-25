import discord
import asyncio
import os
import aiohttp
import logging
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', handlers=[logging.StreamHandler()])

PROXY_URL = os.getenv("PROXY_URL")
client = discord.Client(intents=discord.Intents.default())
last_event_time = datetime.now(timezone.utc)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user} (ID: {client.user.id})")
    print("🚀 Bot ready - monitoring joins...")
    logging.info(f"Connected at {datetime.now(timezone.utc)}")

@client.event
async def on_member_join(member):
    global last_event_time
    if member.bot: return
    last_event_time = datetime.now(timezone.utc)
    message = f"**{member.guild.name}** » {member} (ID: {member.id}) joined!"
    print(f"👤 {message}")
    channel = client.get_channel(1483149225134133429)
    if channel: await channel.send(message)

@client.event
async def on_disconnect():
    logging.warning("❌ Disconnected - reconnecting...")

class ProxyConnector(aiohttp.TCPConnector):
    def __init__(self, proxy_url):
        super().__init__(limit=100)
        self.proxy_url = proxy_url

async def health_check():
    while not client.is_closed():
        await asyncio.sleep(300)
        idle_time = (datetime.now(timezone.utc) - last_event_time).total_seconds()
        if idle_time > 1800:
            logging.warning(f"⚠️ Idle {idle_time/60:.0f}min - reconnecting")
            await client.close()

async def run_bot():
    fails = 0
    while True:
        try:
            print(f"🔄 Connecting (attempt {fails+1})")
            connector = ProxyConnector(PROXY_URL) if PROXY_URL else None
            if PROXY_URL: print(f"🌐 IPRoyal: {PROXY_URL[:40]}...")
            await asyncio.gather(client.start(os.getenv("DISCORD_TOKEN"), bot=False, connector=connector), health_check())
        except Exception as e:
            fails += 1
            logging.error(f"💥 {type(e).__name__}: {e}")
            await asyncio.sleep(15 if fails < 5 else 300)

if __name__ == "__main__":
    print("🎯 IPRoyal Discord Join Monitor")
    asyncio.run(run_bot())
