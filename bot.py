from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd
from comand import *

bot = Bot(token='5794724862:AAHwlwX_rPzpdhKkbzBGefWt12OAvmqJYBs')
updater = Updater(token='5794724862:AAHwlwX_rPzpdhKkbzBGefWt12OAvmqJYBs')
dispatcher = updater.dispatcher



del_abv = CommandHandler('del', take_text) 

dispatcher.add_handler(del_abv)


updater.start_polling()
updater.idle()