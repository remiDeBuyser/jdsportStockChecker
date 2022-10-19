import time

import requests as requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
import time

toast = ToastNotifier()

URL = "https://www.jdsports.fr/product/noir-nike-sweat--capuche-foundation-full-zip-homme/16011261_jdsportsfr/stock/"
# URL = "https://www.jdsports.fr/product/gris-adidas-originals-sweat--capuche-graffiti-homme/16543485_jdsportsfr/stock/"



con = True
while con:
    page = requests.get(URL, timeout=10000)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="productSizeStock")
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    if results != None :
        stocks = results.find_all("button")
        for element in stocks:
            stock = len(element.find_all("span", class_="noStockOverlay"))
            if stock == 0:
                toast.show_toast(
                    "JDSport",
                    "Du stock a été ajouté",
                    duration=10,
                    threaded=True
                )
    time.sleep(29)
