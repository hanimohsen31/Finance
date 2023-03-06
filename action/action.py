import requests
from bs4 import BeautifulSoup
import datetime
import pytz

# pip install pyTelegramBotAPI
# pip install decouple
# pip install requests
# pip install beautifulsoup4
# pip install pytz

def getPrices():
    dataReaquired = [
        {"title": "5gm", "url": "https://shop.btcegyptgold.com/24k-gold-islamic-ingot-al-kursi-verse-5g.html",
            "class": "price", "index": 1},
        {"title": "10gm", "url": "https://shop.btcegyptgold.com/24k-pharaonic-king-tut-yellow-gold-ingot-10.html",
            "class": "price", "index": 1},
        {"title": "20gm", "url": "https://shop.btcegyptgold.com/24k-btc-yellow-gold-ingot-20-g.html",
            "class": "price", "index": 1},
        {"title": "31.1gm", "url": "https://shop.btcegyptgold.com/24k-i-love-you-gold-ingot-31-1g.html",
            "class": "price", "index": 1},
        {"title": "50gm", "url": "https://shop.btcegyptgold.com/24k-pharaonic-queen-nefertari-yellow-gold-ingot-50-g.html",
            "class": "price", "index": 1},
        {"title": "Dollar Now", "url": "https://www.google.com/finance/quote/USD-EGP?hl=en",
         "class": "YMlKec fxKbKc", "index": 0},
    ]
    dataToShow = []
    for i in dataReaquired:
        page = requests.get(i.get("url"))
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(class_=i.get("class"))[i.get("index")].text
        # print(price)
        dataToShow.append({i.get("title"): price})
    return dataToShow


def reply():
    prices = getPrices()
    url = 'https://finance-456dd-default-rtdb.firebaseio.com/Data.json'
    x = requests.get(url)
    y = x.json()
    time2 = str(datetime.datetime.now(pytz.timezone('Africa/Cairo')).strftime("%Y-%m-%d %I:%M %p"))
    firebaseObj = {
        "Date": time2,
        'G5gm': prices[0]['5gm'].replace(",", ".").replace(" EGP", ""),
        'G10gm': prices[1]['10gm'].replace(",", ".").replace(" EGP", ""),
        'G20gm': prices[2]['20gm'].replace(",", ".").replace(" EGP", ""),
        'G31gm': prices[3]['31.1gm'].replace(",", ".").replace(" EGP", ""),
        'G50gm': prices[4]['50gm'].replace(",", ".").replace(" EGP", ""),
        'Dollar': prices[5]['Dollar Now'].replace(",", ".").replace(" EGP", "")
    }
    y.append(firebaseObj)

    requests.put(url=url, json=y)
    newPrices = ""
    for i in prices:
        newPrices = newPrices + "\n" + str(i)
    newPrices = newPrices.replace("[", "").replace(
        "]", "").replace("{", "").replace("}", "").replace("'", "")
    
    return newPrices

reply()
