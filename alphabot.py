import os
import telepot
from telepot.loop import MessageLoop
bot = telepot.Bot('5054953100:AAGHRjM3wbs8LnwkkcZSBpPCQwBtxZnF38Q')
bot.getMe()
from pprint import pprint
response = bot.getUpdates()
pprint(response)


def handle(msg):
    pprint(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    if msg['text'] =='/command1':
        bot.sendMessage(chat_id,'anggugu')

    else:
        if msg['text'] =='/command2':
         bot.sendMessage(chat_id,'heihei')

    if msg['text'] =='/command3':
        bot.sendMessage(chat_id,'amagi')

    if msg['text'] =='/command4':
        bot.sendMessage(chat_id,'qiubabi')


TOKEN = '5054953100:AAGHRjM3wbs8LnwkkcZSBpPCQwBtxZnF38Q'
MessageLoop(bot, handle).run_forever()

