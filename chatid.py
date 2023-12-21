import asyncio
import os

try:
    import telegram
    from telegram import *
except ModuleNotFoundError:
    os.system('pip install python-telegram-bot --upgrade')
    print('recommended to restart program')

bot_token = str(input("\n \ninput telegram bot token again and copy your id \n"))

async def main():
    bot = telegram.Bot(bot_token)
    async with bot:
        updates = (await bot.get_updates())[0]
        print(updates)

if __name__ == '__main__':
    asyncio.run(main())
print()
print()
cht_id = str(input("copy and paste the chat id here \n"))