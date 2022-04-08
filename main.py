import requests
from bs4 import BeautifulSoup
import telebot

bot = telebot.TeleBot(token="5081203527:AAEW_OyeTo9x52-dXx1ltrnGTQl_atdrFjs")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """Привет! Я бот, который позволит быстро находить обои в <b><a href="https://wallpapers.com/">Wallpapers</a></b>
Для того, чтобы получить обои, введи его название в поле...""",
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
