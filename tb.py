import os
import telebot
import reddit
import constants

TELEGRAM_API_KEY = constants.TELEGRAM_API_KEY


# TELEGRAM_API_KEY = os.environ['TELEGRAM_API_KEY']
bot = telebot.TeleBot(TELEGRAM_API_KEY)


@bot.message_handler(commands=['greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")


@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

def send_images(message):
  request = message.text.split()
  if len(request) < 3 or request[0].lower() not in "send" or isinstance(request[2],int) :
    return False
  else:
    return True

@bot.message_handler(func=send_images)
def send_images(message):
  subreddit = message.text.split()[1]
  try:
    number_of_posts = int(message.text.split()[2])
    list_of_urls = reddit.get_images(subreddit,number_of_posts)
    if len(list_of_urls) < number_of_posts:
      list_of_urls = reddit.get_images(subreddit,number_of_posts + 1)
      # print(list_of_urls)
      # print(number_of_posts)
    # print(list_of_images)
    for url in list_of_urls:
        # print(url)
        # print(url.split('.')[-1])
        if url.split('.')[-1] == 'jpg' :
          bot.send_photo(message.chat.id, url)
        elif url.split('.')[-1] == 'gif':
          bot.send_animation(message.chat.id, url)
        else:
          bot.send_video(message.chat.id, url)
    # bot.send_photo(message.chat.id, 'https://media.wired.com/photos/5b899992404e112d2df1e94e/master/pass/trash2-01.jpg')
  except ValueError as err:
    print('ValueError', err)


while True:
  try:
    bot.polling()
  except Exception:
    print(Exception)
    