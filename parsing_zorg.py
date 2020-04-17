import requests
import discord
from pyaspeller import YandexSpeller
import pastebin

TOKEN = "Njk4MDg2ODcxMDI4NDY1Njk1.XpmrRQ."
TOKEN2 = "j6kzBOwG8CsrlHUe9p9oCKSt8Jw"
TOKEN = TOKEN + TOKEN2

t = []
client = discord.Client()


def is_me(m):
    return m.author == client.user


def translate(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20200409T191416Z.e9897b968ea45216.fc831592f623388daee7313eed3091868362dacc'
    lang = 'kk-uk'
    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
    # Выводим результат
    r = r.text[36:]
    r = r.replace('"]}', "")
    return r


def spel(text):
    speller = YandexSpeller(lang="ru", ignore_urls=True,
                            ignore_tags=True,
                            ignore_capitalization=True,
                            ignore_digits=True,
                            ignore_latin=True,
                            ignore_roman_numerals=True,
                            ignore_uppercase=True,
                            find_repeat_words=False)
    try:
        changes = {change["word"]: change["s"][0] for change in speller.spell(text)}
        for word, suggestion in changes.items():
            text = text.replace(word, suggestion)
        return text
    except Exception as e:
        text = "О, семпай использовал запретное заклинание! Нехорошо так делать."
        return text


@client.event
async def on_message(message):
    channel = message.channel

    if message.content.startswith('вспышка'):
        deleted = await channel.purge(limit=1000, check=is_me)

    elif message.content.startswith('взрыв'):
        deleted = await channel.purge(limit=10)

    elif message.content.startswith('бабах'):
        deleted = await channel.purge(limit=50)

    elif message.content.startswith('бум'):
        deleted = await channel.purge(limit=500)

    elif message.content.startswith('explosion'):
        deleted = await channel.purge()
        await channel.send("Explosion, power unlimited")

    elif message.content.startswith('help'):
        await channel.send("вспышка - удалить сообщения бота\n"
                           "взрыв - удалить 10 последних сообщений\n"
                           "бабах - удалить 50 последних сообщений\n"
                           "бум - удалить 500 последних сообщений\n"
                           "explotion - взрыв невероятной мощи")
    elif message.content.startswith("бух"):
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith('путешественник Бот'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "Groovy":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith('путешественник Назаров'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "NikitaNazarov":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith('путешественник Артем'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "Артём Пойдашев":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith("спам"):
        for i in range(100):
            await message.channel.send("спам")

    elif message.content.startswith('путешественник Ваня'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "genii":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith('путешественник Даня'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "sabberian":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith('путешественник Макс'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "Max_TM5757":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith('путешественник Ярик'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "Ярик":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith('путешественник Камиль'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "kamjx":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith('путешественник Женя'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "Евгения":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith('путешественник Леня'):
        category = client.get_channel(700051337617997864)
        for x in range(10):
            await category.create_voice_channel("Измерение " + str(x))

        guild = client.get_guild(578239094342287371)
        for mem in guild.members:
            if mem.name == "Daz":
                jus = mem
        channels = category.channels
        for i in range(2):
            for x in channels:
                await jus.edit(voice_channel=x)
        await jus.edit(voice_channel=client.get_channel(700060441988169878))
        guild = client.get_guild(578239094342287371)
        channels = guild.channels
        for x in channels:
            if "Измерение" in x.name:
                await x.delete()

    elif message.content.startswith("спам"):
        for i in range(100):
            await message.channel.send("спам")



    elif message.author.id != 698086871028465695:
        text = spel(message.content)
        await message.channel.send(text)


@client.event
async def on_ready():
    print("Мы готовы, командир!")
    guild = client.get_guild(578239094342287371)
    channels = guild.channels
    for x in channels:
        if "Измерение" in x.name:
            await x.delete()


client.run(TOKEN)
