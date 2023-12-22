import os
try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
def get_chat_id(TOKEN):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    a=(requests.get(url).json())['result'][0]['message']['from']['id']
    return a
b = input("paste bot token after messaging the bot\n")
print()
print(get_chat_id(b))
c = input("copy the chat id too and save it") # to give time to save to clipboard
