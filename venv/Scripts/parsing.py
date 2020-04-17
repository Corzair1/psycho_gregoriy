from grab import *
import time
import os
import urllib
def get_img(img_link_list):
    for x in img_link_list:
        # Получаем параметр src тега img
        img_url = str(x.get('href'))
        # Исправляем ссылку
        # img_url = img_url.replace('.240.', '.full.')
        # img_url = img_url.replace('s3.', 'static.')
        # Скачиваем изображение
        img = urllib.urlopen(img_url).read()
        # Пусть его именем станет его номер и расширение
        img_name = img_url.split('.')[len(img_url.split('.')) - 2] +  '.'+ img_url.split('.')[len(img_url.split('.')) - 1]
        # Если такой файл уже существует, удаляем к чертям
        if os.path.isfile(img_name): os.remove(img_name)
        # Сохраняем, закрываем, ждём дабы нас не послали за попытку         DDOS`a
        f = open(img_name, "wb")
        f.write(img)
        f.close()
        time.sleep(0.4)
quote='аниме тян'
quoteURL=urllib.quote(quote)
g = Grab(log_file='out.html')
g.setup(hammer_mode=True, hammer_timeouts=((2, 5), (10, 15), (20, 30)))
#g.setup(connect_timeout=50, timeout=50)
g.go('http://images.google.com/images?hl=ru&q='+quoteURL+'&sa=N&start=$p&ndsp=20&sout=1')
get_img(g.doc.select('//a[@class="b-serp-image c-loaded"]'))

#get_img(g.xpath_list('//a[@class="b-serp-image c-loaded"]'))