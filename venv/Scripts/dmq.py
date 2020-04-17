import requests
import time
import sys

def translate():
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20200409T191416Z.e9897b968ea45216.fc831592f623388daee7313eed3091868362dacc'
    r = requests.get("https://translate.yandex.net/api/v1.5/tr/getLangs", data={"key" : key})
    print(r.text.replace("string", ""))

translate()