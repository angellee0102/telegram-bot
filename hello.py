from telegram.ext import Updater, CommandHandler
from random import sample
from itertools import combinations
from nctu import nctu_introtext, nctu_readmore
from weather_test import today_weather, tomorrow_weather, afterTomorrow_weather
import os

print(os.environ.get('TELEGRAM_BOT_TOKEN'))
print (os.environ['WEATHER_API'])
print (os.environ['TELEGRAM_BOT_TOKEN'])
def valid(s):
    if len(s)!=4:
        return False
    if any(x not in '0123456789' for x in s):
        return False
    if any(x==y for x, y in combinations(s,2)):
        return False
    return True

ans=''.join(sample('0123456789',4))
def hello(bot, update):
    update.message.reply_text(
        '你好 hello, {}'.format(update.message.from_user.first_name))

def new_game(bot,update):
    ans=''.join(sample('0123456789',4))
    print('answer',ans)
    update.message.reply_text('Let\'s start a new game')

def guess(bot, update):
    toks=update.message.text.strip().split()
    print('toks',toks)
    if len(toks)!=2:
        msg='Wrong format!'
    elif valid(toks[1]) == False:
        msg='{} is valid'.format(toks[1])
    else:
        A = sum(1 for x,y in zip(toks[1],ans) if x==y)
        B = sum(1 for x in toks[1] if x in ans)-A
        result='{}A{}B'.format(A,B)
        msg='{} is {}'.format(toks[1], result)
        
    update.message.reply_text(msg)

def bye(bot, update):
    update.message.reply_text(
        'bye bye, {}'.format(update.message.from_user.first_name))
def show_text(bot, update):
    text=update.message.text
    print('Received: ', text)
    update.message.reply_text(
        'echo:  {}'.format(update.message.text))

def nctu(bot, update):
    nctu_intro=nctu_introtext()
    nctu_link=nctu_readmore()
    nctu_result=nctu_intro+nctu_link
    update.message.reply_text('{}'.format(nctu_result))
def weather(bot, update):
    today=today_weather()
    tomorrow=tomorrow_weather()
    afterTomorrow=afterTomorrow_weather()

    weather_result=today+tomorrow+afterTomorrow
    update.message.reply_text('{}'.format(weather_result))
token=os.environ["TELEGRAM_BOT_TOKEN"]    
updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('bye', bye))
updater.dispatcher.add_handler(CommandHandler('content', show_text))
updater.dispatcher.add_handler(CommandHandler('new', new_game))
updater.dispatcher.add_handler(CommandHandler('guess', guess))
updater.dispatcher.add_handler(CommandHandler('nctu', nctu))
updater.dispatcher.add_handler(CommandHandler('weather', weather))

updater.start_polling()
updater.idle()