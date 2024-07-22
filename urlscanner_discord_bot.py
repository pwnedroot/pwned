import discord
from discord.ext import commands
import requests

# Replace with your actual bot token
BOT_TOKEN = 'your_discord_bot_token_here'

# Replace with your VirusTotal API key
API_KEY = 'your_virus_total_api_here'

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        url_to_scan = extract_url(message.content)
        if url_to_scan:
            await scan_url(message.channel, url_to_scan)
        else:
            await message.channel.send("No valid URL found in the message.")

    await bot.process_commands(message)

async def scan_url(channel, url):
    try:
        url_scan = 'https://www.virustotal.com/vtapi/v2/url/scan'
        url_report = 'https://www.virustotal.com/vtapi/v2/url/report'
        params_scan = {'apikey': API_KEY, 'url': url}

        response_scan = requests.post(url_scan, data=params_scan)
        json_response_scan = response_scan.json()

        if response_scan.status_code == 200:
            scan_id = json_response_scan.get('scan_id')

            params_report = {'apikey': API_KEY, 'resource': url, 'scan_id': scan_id}
            response_report = requests.get(url_report, params=params_report)
            json_response_report = response_report.json()

            permalink = json_response_report.get('permalink')

            await channel.send(f"View Full Report: {permalink}")

        else:
            await channel.send(f"Failed to submit scan request. Status code: {response_scan.status_code}")

    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        print(error_message)
        await channel.send(error_message)

def extract_url(message_content):
    # Extracts the first URL found in the message content
    words = message_content.split()
    for word in words:
        if word.startswith("http://") or word.startswith("https://"):
            return word
    return None

bot.run(BOT_TOKEN)
