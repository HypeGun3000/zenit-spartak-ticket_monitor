import requests
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook

cookies = {
    #***
}

headers = {
    #***
}

new_sectors = []
new_sector_good = []

while True:
    response = requests.get(
        'https://spb.kassir.ru/sport/stadion-sankt-peterburg-59b8fab76db7a/olimpbet-superkubok-rossii-zenit-spartak-2022-2022-07-09',
        cookies=cookies, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    all_sectors = soup.find_all(class_='col-sector')
    all_prices = soup.find_all(class_='col-amount')
    for index, sector in enumerate(all_sectors):
        if sector.text.strip().split(' ')[0] not in new_sectors and sector.text.strip().split(' ')[0] != 'Сектор':
            webhook = DiscordWebhook(
                url='###',
                content=f'Сектор : {sector.text.strip().split(" ")[0]} \nПОЯВИЛСЯ НОВЫЙ СЕКТОР! \nКол-во билетов : {all_prices[index].text.strip()}')
            new_sectors.append(sector.text.strip().split(' ')[0])
            response = webhook.execute()
        if sector.text.strip().split(' ')[0][1] == '1' and sector.text.strip().split(' ')[0][0] in 'adc' and sector.text.strip().split(' ')[0] not in new_sector_good:
            webhook = DiscordWebhook(url='###',
                                     content=f'Сектор : {sector.text.strip().split(" ")[0]} \nКол-во билетов : {all_prices[index].text.strip()} \nhttps://spb.kassir.ru/sport/stadion-sankt-peterburg-59b8fab76db7a/olimpbet-superkubok-rossii-zenit-spartak-2022-2022-07-09 \n@everyone')
            response = webhook.execute()
            new_sector_good.append(sector.text.strip().split(' ')[0])
            time.sleep(2)
    print('Searching...')
    time.sleep(10)
