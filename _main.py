# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import discord
from selenium.webdriver.chrome.options import Options
import sys
import requests

b = []
y = ""

options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.


client = discord.Client()

TOKEN = "NjkzMDQ0MTA0NzUzNDQ3MDMy.Xn3Zog.Tot4YTG0kCL7NP4fLEjrPiRUzek"


address = "http://iplayif.com/?story=http%3A%2F%2Fwww.ifarchive.org%2Fif-archive%2Fgames%2Fzcode%2Fzdungeon.z5"

driver = webdriver.Chrome(chrome_options=options, executable_path='C:\\chromedriver_mac64\chromedriver.exe')
driver.get(address)

for element in driver.find_elements_by_tag_name("span"):
    y += element.text + "\n"


def translate(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20200409T191416Z.e9897b968ea45216.fc831592f623388daee7313eed3091868362dacc'
    lang = 'en-ru'
    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
    # Выводим результат
    r = r.text[36:]
    r = r.replace("", "")
    return r

def translate_2(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20200409T191416Z.e9897b968ea45216.fc831592f623388daee7313eed3091868362dacc'
    lang = 'ru-en'
    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
    r = r.text[36:]
    r = r.replace('"]}', "")
    return r


def answer(a):
    global b
    b = []
    print(a)
    if a == "stop":
        go_away()

    PUTIN = driver.find_element_by_class_name("TextInput")
    PUTIN.send_keys(a + "\n")

    time.sleep(5)

    for element in driver.find_elements_by_tag_name("span"):
        b.extend(element.text.replace(">", "🦝").split("\n"))


def go_away():
    sys.exit()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(695202855107297352)
    await channel.send("Это мой бот для игры в текстовый квест Зорк, игры созданной в MIT в 1986 году. В игре присутствует встроенный переводчик, основанный на API яндекса.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('play'):
        await message.channel.send("Fuck you for playing this game")

    else:
        channel = client.get_channel(695202855107297352)
        answer(translate_2(message.content))
        g = ""
        for i in range(len(b)):
            g += b[i] + ":назарив:"
        if len(g) >= 2000:
            g = g[(len(g) - (len(g) % 2000)):]
        print(g)
        g = translate(g)
        g = g.replace(":назарив:", "\n")
        g = g.replace('"]}', "")
        await channel.send(g)


client.run(TOKEN)

