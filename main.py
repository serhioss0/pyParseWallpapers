import requests
from bs4 import BeautifulSoup
import telebot

bot = telebot.TeleBot(token="")
headers = {
    'User-Agent': ''
}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """Hey! I am a bot that allows you to quickly find wallpapers in <b><a href="https://wallpapers.com/">Wallpapers</a></b>
In order to get a wallpaper, enter its name in the field...""",
                     parse_mode="html", disable_web_page_preview=1)


@bot.message_handler(content_types=['text'])
def parse(message):
    index = 0
    url = "https://wallpapers.com/" + message.text
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    all_links = soup.find_all('li', class_="card content")
    for index, link in enumerate(all_links):
        bot.send_message(message.chat.id, "https://wallpapers.com/" + link.img['data-src'])
        if index == 9:
            break


if __name__ == '__main__':
    bot.polling(none_stop=True)
