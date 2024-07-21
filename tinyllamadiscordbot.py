import discord
from discord.ext import commands
import asyncio
import textwrap
import ollama  # Make sure ollama module is installed: pip install ollama

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user.name}")

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("I'm Here!")

@bot.command(name="ask")
async def ask(ctx, *, message):
    # Display typing indicator
    typing_indicator = await ctx.send("Typing...")

    try:
        # Simulate processing time
        await asyncio.sleep(3)  # Replace with actual processing time if needed

        # Generate response
        response = ollama.chat(model='tinyllama', messages=[
            {
                'role': 'user',
                'content': message,
            },
        ])

        # Send response, handling long messages
        await send_long_message(ctx, response['message']['content'])

    finally:
        # Remove typing indicator
        await typing_indicator.delete()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

async def send_long_message(destination, content):
    max_length = 2000
    chunks = textwrap.wrap(content, width=max_length, replace_whitespace=False)
    for chunk in chunks:
        await destination.send(chunk)

# Replace the token with your own bot token
bot.run("enteryourdiscordbottokenrighthere")

