## PRICE TRACKER BOT

Price tracker in Python custom made for Eneba.com. It was build to obtain Metroid Dread at a low prize. You need to custom `URL` variable and `getPrice()` function in order for this bot to work property in other websites.

```python
def getPrice():
    page = requests.get(URL, headers=HEADER) #URL is from eneba.com
    soup = BeautifulSoup(page.content, "html.parser")

    #these two html classes were extracted after inspecting metroid dread shoping page on Eneba
    title = soup.find(class_="pO0YjY").get_text().strip()
    price = soup.find(class_="L5ErLT").get_text().strip()[0:2] # Coge los dos primeras posiciones del string como si fuese un array, sin contar la ultima. 0 y 1

    print('-----------------------------------------------------')
    print(title)
    print(price+"\n")
    return price
```

> :warning: **NOTE:** You also need to change directory route in `priceTrackerInicio.bat` after cd. This bat was made to automate price tracker bot after pc boot.

