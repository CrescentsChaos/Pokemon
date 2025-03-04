from importlist import *
#intents=discord.Intents.default()
#intents.members=True
#intents.reactions=True
#intents.message_content=True
prefix="!"
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd,activity=discord.Game("Pokémon"))
    print(f"We have logged in as {bot.user}")
    try:
        synced=await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)!")
    except:
        print(Exception)
