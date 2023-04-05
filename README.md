## PRICE TRACKER BOT

> :rotating_light: The Eneba HTML structure has changed since this project was released. Refer to [Issues](https://github.com/DviadFer/priceTrackerEneba/issues) to further info on this topic.

A custom Python price tracker made for Eneba.com, designed to obtain products at lower prices. To make this bot work properly on other websites, you need to customize the `URL` variable and `getPrice()` function.

```python
def getPrice():
    page = requests.get(URL, headers=HEADER) #URL in this case: eneba.com
    soup = BeautifulSoup(page.content, "html.parser")

    # These two HTML classes were extracted after inspecting the product shopping page on Eneba
    # You should adapt your soup.find() query to your specific case.
    title = soup.find(class_="pO0YjY").get_text().strip()
    price = soup.find(class_="L5ErLT").get_text().strip()[0:2] 
	# [...]
    return price
```

> :warning: **NOTE:** You also need to change the directory path in `priceTrackerInicio.bat` after `cd` within its code. This batch file was created to automate the price tracker bot after PC boot.

