import os
import asyncio
file = open("user data.txt",'r')
if os.stat(file).st_size == 0:
    file = open("user data.txt",'w')
    print("follow instruction page to set this \n if you do not wish to use a telegram bot\n use test.py directly")
    import chatid
    bot_token = chatid.bot_token
    cht_id = chatid.cht_id
    file.write(bot_token+"\n"+cht_id)
    file.close()

import test
try:
    import telegram
    from telegram import *
except ModuleNotFoundError:
    os.system('pip install python-telegram-bot --upgrade')
    print('recommended to restart program')
A = test.A
print(A)


content = file.readline()
bot_token = str(content[0])
cht_id = int(content[1])
async def main():
    bot = telegram.Bot(bot_token)
    async with bot:
        await bot.send_message(text=('Test report for '+ A) , chat_id=cht_id)
        await bot.send_photo(cht_id, photo=open(("test"+A+"\\"+"test time"+A+".png"), 'rb'))
        await bot.send_photo(cht_id, photo=open(("test"+A+"\\"+"test result"+A+".png"), 'rb'))
        await bot.send_document(cht_id,("test"+A+"\\"+"test"+A+".xlsx"))

if __name__ == '__main__':
    asyncio.run(main())