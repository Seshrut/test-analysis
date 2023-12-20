import test
import asyncio
import telegram
A = test.A
print(A)
async def main():
    bot = telegram.Bot("6105380010:AAE7r3p0A3T3qGtBk70qyEWplsRfgA-siMU")
    async with bot:
        await bot.send_message(text=('Test report for '+ A) , chat_id=5036914302)
        await bot.send_photo(5036914302, photo=open(("D:\\Seshrut\\Error-505!!\\Tests\\"+"test"+A+"\\"+"test time"+A+".png"), 'rb'))
        await bot.send_photo(5036914302, photo=open(("D:\\Seshrut\\Error-505!!\\Tests\\"+"test"+A+"\\"+"test result"+A+".png"), 'rb'))
        await bot.send_document(5036914302,("D:\\Seshrut\\Error-505!!\\Tests\\"+"test"+A+"\\"+"test"+A+".xlsx"))

if __name__ == '__main__':
    asyncio.run(main())