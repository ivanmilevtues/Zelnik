import schedule
import time

from discord.ext.commands import Bot

TOKEN = ""

BOT_PREFIX = ("!") # you can add more prefixes in a set


client = Bot(BOT_PREFIX)

@client.command(name="obqd")
async def time_for_lunch():
    await client.say("@everyone Време е за обяд кучета!")

schedule.every().day.at("22:54").do(time_for_lunch)

client.run(TOKEN)

while True:
    schedule.run_pending()