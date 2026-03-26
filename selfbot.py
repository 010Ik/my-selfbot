import discord
import asyncio
import os
from datetime import datetime, timezone

client = discord.Client()

@client.event
async def on_ready():
    print(f"[{datetime.now(timezone.utc)}] Hi! I'm logged in as {client.user} (ID: {client.user.id})")
    print("Bot is ready and monitoring server joins...")

@client.event
async def on_member_join(member):
    if member.bot:
        return

    message = f"[{member.guild.name}] {member} (ID: {member.id}) just joined!"
    print(f"[{datetime.now(timezone.utc)}] {message}")

    # Send to your notification channel
    channel = client.get_channel(1483149225134133429)   # ← YOUR CHANNEL ID
    if channel is not None:
        await channel.send(message)
    else:
        print(f"DEBUG: Channel not found! Check ID: 1483149225134133429")

# Run the bot
if __name__ == "__main__":
    asyncio.run(client.start(os.getenv("TOKEN")))
