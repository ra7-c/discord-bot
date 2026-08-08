import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    channel_id = 1341457814349144124  # أي دي الروم الصوتي حقك
    channel = bot.get_channel(channel_id)
    if channel:
        try:
            await channel.connect()
            print("Connected to voice channel!")
        except Exception as e:
            print(f"Failed to connect: {e}")
    else:
        print("Voice channel not found!")

bot.run("MTUzNTc1Nju3MTA1NTc1NTM5NC5GX2E0rn.8fggUZOCA-PW27_nNtLDsnaJEjRaQ3ilqFMmTQ")
