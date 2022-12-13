## PRICE TRACKER BOT

> :rotating_light: Eneba html structure has changed since this project was released. Refer to [Issues](https://github.com/DviadFer/priceTrackerEneba/issues) to further info on this topic.

Price tracker in Python custom made for Eneba.com. It was build to obtain Metroid Dread at a low prize. You need to customize `URL` variable and `getPrice()` function in order for this bot to work property in other websites.

```python
def getPrice():
    page = requests.get(URL, headers=HEADER) #URL is from eneba.com
    soup = BeautifulSoup(page.content, "html.parser")

    #these two html classes were extracted after inspecting metroid dread shoping page on Eneba
    #You should adapt your soup.find() query to your specific case.
    title = soup.find(class_="pO0YjY").get_text().strip()
    price = soup.find(class_="L5ErLT").get_text().strip()[0:2] 
	# [...]
    return price
```

> :warning: **NOTE:** You also need to change directory route in `priceTrackerInicio.bat` after cd. This bat was made to automate price tracker bot after pc boot.

