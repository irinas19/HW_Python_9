from turtle import update
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd


def take_text(update, context):
    lang = ['а', 'б', 'в']
    text = update.message.text.split(' ')
    tamp = -1
    for i in text:
        tamp += 1
        count = 0
        for j in i:
            if str(j) in lang:
                count += 1
            if count == 3:
                text[tamp] = ''
    text = list(filter(lambda a: a != '' and a != '/del', text))
    context.bot.send_message(update.effective_chat.id, ' '.join(text))


