from telethon import TelegramClient
import logging
import time

api_id ="1125689"
api_hash ="4772d1792ed194020a8fb06a91ffb8fa"
bot_token ="6239932587:AAHcZMHo9-4FwD7kV8c6reGdtQFcVWrH45c"
bot =  TelegramClient("barwar", api_id, api_hash).start(bot_token=bot_token)