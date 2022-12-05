import os
import telebot
import reddit

TELEGRAM_API_KEY = '5686571609:AAEZKdfpDpbH_cdnvznVbKICgXewutuO6hc'


# TELEGRAM_API_KEY = os.environ['TELEGRAM_API_KEY']
bot = telebot.TeleBot(TELEGRAM_API_KEY)


@bot.message_handler(commands=['greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")


@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

# def send_images(message):
#   request = message.text.split()
#   if len(request) < 3 or request[0].lower() not in "send":
#     return False
#   else:
#     return True

# @bot.message_handler(commands=['send'])
# def send_images(message):
#   list_of_images = reddit.send_images('greentext',5)
#   for image in list_of_images:
#     bot.send_photo(message.chat.id, image)

bot.infinity_polling()