import requests
from bs4 import BeautifulSoup 
import time
import csv
from fake_useragent import UserAgent

store_city = []
store_town = []
store_name = []
store_addr = []

ua = UserAgent()
header = {"User-Agent":ua.random, "Referer": "https://www.watsons.com.tw/store-finder"}
for i in range(1, 60):
    print(i)
    params = {
        "currentPage": i,
        "town": "",
        "district":"" ,
        "features": "",
        "keyword": ""
    }
    url = "https://www.watsons.com.tw/store-finder/getPartialStore?"
    res = requests.get(url, params=params, headers=header, timeout=10)
    print(res.status_code)
    html = res.text
    #print(html)

    soup = BeautifulSoup(html.replace("\n", "").strip(), "html.parser")
    
    item_city = soup.find_all("font", class_="shopTown")
    for city in item_city:
        store_city.append(city.text)
        print(store_city)
    time.sleep(1)
    item_town = soup.find_all("font", class_="shopDistrict")
    for town in item_town:
        store_town.append(town.text)
        print(store_town)
    
    item_name = soup.find_all("font", class_="resultShopName")
    for name in item_name:
        store_name.append(name.text)
        print(store_name)
    time.sleep(1)
    item_addr = soup.find_all("font", class_="shopStreetName")
    for name in item_addr:
        store_addr.append(name.text)
        print(store_addr)

with open('storelist_watsonsv3.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['城市', '區域', '門市名稱', '門市地址']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_city)):
        newrow.clear()
        newrow.append(store_city[n])
        newrow.append(store_town[n])
        newrow.append(store_name[n])
        newrow.append(store_addr[n])
        csvwriter.writerow(newrow)



