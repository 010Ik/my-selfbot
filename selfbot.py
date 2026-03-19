import discord

# Create the self-bot (no intents needed)
client = discord.Client()

@client.event
async def on_ready():
    print(f"Hi! I'm logged in as {client.user} (my ID is {client.user.id})")
    print("Waiting for people to join servers... (Ctrl+C to stop)")

@client.event
async def on_member_join(member):
    if member.bot:
        return

    message = f"[{member.guild.name}] {member} (ID: {member.id}) just joined!"
    print(message)

    # Optional: Send to your own channel (change the number if you want)
    channel_id = 1483149225134133429
    channel = client.get_channel(1483149225134133429)
    if channel is not None:
    await channel.send(message)
else:
print(f"DEBUG: Channel not found! Check ID: {channel_id}")

# Your token here (keep the quotes!)
import os
client.run(os.getenv("TOKEN"))
