import discord
import subprocess
import os

TOKEN = 'your_discord_bot_token_right_here'
GUILD_ID = 'YOUR_GUILD_ID'  # Optional: Specify the guild ID if you want to limit the bot to a specific server

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!checkphone'):
        phone_number = message.content.split(' ')[1]

        # Ensure the Bash script is executable
        os.chmod('check_phone.sh', 0o755)

        # Execute the Bash script with the phone number, automatically prepending '+1'
        result = subprocess.run(['./check_phone.sh'], input=phone_number.encode(), stdout=subprocess.PIPE)

        # Get the output from the Bash script
        response = result.stdout.decode()

        # Send the result to the Discord channel
        await message.channel.send(f'Phone number info: {response}')

client.run(TOKEN)

