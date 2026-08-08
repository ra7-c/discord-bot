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
    channel_id = 1341457814349144124  # آي دي الروم الصوتي حقك
    channel = bot.get_channel(channel_id)
    if channel:
        try:
            await channel.connect()
            print("Connected to voice channel!")
        except Exception as e:
            print(f"Failed to connect: {e}")
    else:
        print("Voice channel not found!")

# استبدل هذا التوكن بالتوكن الخاص ببوتك
bot.run("MTUzNTc1NjU3MTA1NTc1NTM5NA.Gutf8G.7gfVthbvUSINd5E1_0xxoQZR-kqc1K-RgSAstQ")
