import requests
from bs4 import BeautifulSoup
import requests
import datetime
import pytz


def getPrices():
    dataReaquired = [
        {"title": "10gm", "url": "https://egypt.gold-era.com/ar/product/%d8%b3%d8%a8%d9%8a%d9%83%d8%a9-%d8%b0%d9%87%d8%a8-10-%d8%ac%d8%b1%d8%a7%d9%85/",
            "class": "woocommerce-Price-amount amount", "index": 3},
        {"title": "Dollar Now", "url": "https://www.google.com/finance/quote/USD-EGP?hl=en",
         "class": "YMlKec fxKbKc", "index": 0},
    ]

    PricesList = []
    for i in dataReaquired:
        # web scrapping
        page = requests.get(i.get("url"))
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(class_=i.get("class"))[i.get("index")].text[0:6:1].replace(",",".")
        print(price)
        # appending data to array
        PricesList.append({i.get("title"): price})
    print("Prices Scrapping Done ...")
    return PricesList


def AssignDataToFirebase():
    prices = getPrices()
    url = 'https://finance-456dd-default-rtdb.firebaseio.com/Data.json'
    firebaseList = requests.get(url)
    firebaseListJson = firebaseList.json()
    date = str(datetime.datetime.now(pytz.timezone(
        'Africa/Cairo')).strftime("%Y-%m-%d %I:%M %p"))
    gmPrice = float((str(prices[0]['10gm'])).replace(
        ",", ".").replace(" EGP", ""))/10
    firebaseObj = {
        "Date": date,
        'G5gm': str(gmPrice * 5).replace(",", ".").replace(" EGP", ""),
        'G10gm': str(gmPrice * 10).replace(",", ".").replace(" EGP", ""),
        'G20gm': str(gmPrice * 20).replace(",", ".").replace(" EGP", ""),
        'G31gm': str(gmPrice * 31.1).replace(",", ".").replace(" EGP", ""),
        'G50gm': str(gmPrice * 50).replace(",", ".").replace(" EGP", ""),
        'Dollar': prices[1]['Dollar Now'].replace(",", ".").replace(" EGP", "")
    }    
    # appending data to array
    firebaseListJson.append(firebaseObj)
    # append data to firebase
    requests.put(url=url, json=firebaseListJson)
    # handelling data preview
    handeledPrices = ""
    for i in prices:
        handeledPrices = handeledPrices + "\n" + str(i)
    handeledPrices = handeledPrices.replace("[", "").replace(
        "]", "").replace("{", "").replace("}", "").replace("'", "")
    print(handeledPrices)
    return firebaseObj


print("Gathering Data ....")
print("Please Wait....")
AssignDataToFirebase()

while True:
    x = input("Enter any or q .... ")
    if x == "q" or x == "Q" or x == 'esc':
        print("Quit ...")
        break
    else:
        print("wait ...")
        AssignDataToFirebase()
