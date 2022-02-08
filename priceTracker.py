import requests #Llama url y obtiene informacion de ellas
from bs4 import BeautifulSoup #Permite obtener elementos de paginas web
import time
import smtplib #Permite enviar correos.
#pip install beatifulSoup4

URL = "https://www.eneba.com/es/metroid-dread-nintendo-switch"
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
PRECIO_IDEAL = 42
EMAIL = "diegoviadfer@gmail.com"
PASS = "wneqyprhdrvlyqfi" #Configurada con google app passwords


def trackPrice():
    price = int(getPrice())
    if price > PRECIO_IDEAL:
        diferencia = price - PRECIO_IDEAL
        print(f"Todavia es {diferencia} euros mas caro.")
    else:
        print("Ha bajado de precio!!!!!!!!!!!!\n")
        sendMail()

def getPrice():
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(class_="pO0YjY").get_text().strip()
    price = soup.find(class_="L5ErLT").get_text().strip()[0:2] # Coge los dos primeras posiciones del string como si fuese un array, sin contar la ultima. 0 y 1
    print('-----------------------------------------------------')
    print(title)
    print(price+"\n")
    return price

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL, PASS)   

    asunto = 'Metroid dread ha bajado de precio!'
    mensaje = 'Entra en el link: '+URL

    msg = f"Subject: {asunto}\n\n{mensaje}"

    server.sendmail(EMAIL, EMAIL, msg) #from:, to: y luego el mensaje
    print('Se ha enviado un email de aviso.')
    server.quit()

if __name__ == '__main__':
    while True:
        trackPrice()
        time.sleep(60)

# <h1 class="pO0YjY" itemprop="name">Metroid Dread Nintendo Switch</h1>