import discord
import asyncio
import os
from datetime import datetime, timezone

client = discord.Client()
last_event_time = datetime.now(timezone.utc)

@client.event
async def on_ready():
    print(f"[{datetime.now(timezone.utc)}] Hi! I'm logged in as {client.user} (ID: {client.user.id})")
    print("Bot is ready and monitoring joins...")

@client.event
async def on_member_join(member):
    global last_event_time
    if member.bot:
        return

    last_event_time = datetime.now(timezone.utc)
    message = f"[{member.guild.name}] {member} (ID: {member.id}) just joined!"
    print(f"[{datetime.now(timezone.utc)}] {message}")

    channel = client.get_channel(1483149225134133429)  # YOUR CHANNEL ID
    if channel is not None:
        await channel.send(message)
    else:
        print(f"DEBUG: Channel not found! ID: {1483149225134133429}")

# Health check: force reconnect if no events for 15 minutes
async def health_check():
    while True:
        await asyncio.sleep(60)  # check every 60 seconds
        idle_time = (datetime.now(timezone.utc) - last_event_time).total_seconds()
        if idle_time > 900:  # 15 minutes
            print(f"[{datetime.now(timezone.utc)}] WARNING: No events received in 15+ minutes. Forcing reconnect...")
            await client.close()

# Main run with auto-reconnect
async def run_bot():
    while True:
        try:
            print(f"[{datetime.now(timezone.utc)}] Starting connection to Discord gateway...")
            await asyncio.gather(
                client.start(os.getenv("TOKEN")),
                health_check()
            )
        except Exception as e:
            print(f"[{datetime.now(timezone.utc)}] Connection error: {type(e).__name__}: {e}. Retrying in 10 seconds...")
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(run_bot())
