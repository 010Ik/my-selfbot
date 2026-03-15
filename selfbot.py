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
    channel = client.get_channel(1479466687416762523)
    await channel.send(message)

# Your token here (keep the quotes!)
client.run("MTI0MDIxNzUzOTE0NjAyNzA1OQ.GZZo3m.-_eKCSpLZo8HvJgynSzaQ1ILD657_TCIxoUKZs")
