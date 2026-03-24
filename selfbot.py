import discord
import asyncio
import os

# Create the self-bot
client = discord.Client()

@client.event
async def on_ready():
    print(f"Hi! I'm logged in as {client.user} (my ID is {client.user.id})")
    print("Bot is ready and waiting for joins...")

@client.event
async def on_member_join(member):
    if member.bot:
        return

    message = f"[{member.guild.name}] {member} (ID: {member.id}) just joined!"
    print(message)

    # Send to your notification channel
    channel_id = 1483149225134133429   # ← Change only if your channel ID changed
    channel = client.get_channel(channel_id)

    if channel is not None:
        await channel.send(message)
    else:
        print(f"DEBUG: Channel not found! Check ID: {channel_id} or bot permissions in server")

# Improved run with automatic reconnect
async def run_bot():
    while True:
        try:
            print("Attempting to connect to Discord...")
            await client.start(os.getenv("TOKEN"))
        except Exception as e:
            print(f"Connection lost: {e}. Reconnecting in 15 seconds...")
            await asyncio.sleep(15)   # Short wait before retry

if __name__ == "__main__":
    asyncio.run(run_bot())
