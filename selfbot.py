import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print(f"[{asyncio.get_event_loop().time():.0f}] Hi! I'm logged in as {client.user} (ID: {client.user.id})")
    print("Bot is ready and monitoring joins...")

@client.event
async def on_member_join(member):
    if member.bot:
        return
    message = f"[{member.guild.name}] {member} (ID: {member.id}) just joined!"
    print(f"[{asyncio.get_event_loop().time():.0f}] {message}")

    channel = client.get_channel(1483149225134133429)  # Your channel ID
    if channel is not None:
        await channel.send(message)
    else:
        print(f"DEBUG: Channel not found! ID: {1483149225134133429}")

# Improved run with better logging and faster reconnect
async def run_bot():
    while True:
        try:
            print("Starting connection to Discord gateway...")
            await client.start(os.getenv("TOKEN"))
        except asyncio.TimeoutError:
            print("Timeout while connecting to gateway. Retrying in 8 seconds...")
            await asyncio.sleep(8)
        except Exception as e:
            print(f"Connection error: {type(e).__name__}: {e}. Retrying in 8 seconds...")
            await asyncio.sleep(8)

if __name__ == "__main__":
    asyncio.run(run_bot())
