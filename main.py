import requests
import smtplib
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url="https://www.amazon.com/Slayer-Extended-Non-Slip-Rubber-2T-SBD-27/dp/B0BNNHZY8P/ref=sr_1_25_sspa?keywords=anime%2Baccessories&qid=1700512050&sr=8-25-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1", headers=header)
amazon = response.text
soup = BeautifulSoup(amazon, "html.parser")

#print(soup.prettify())
price = float(soup.find(name="span", class_="a-offscreen").text.split("$")[1])

if price < 25:
    my_gmail = "boydanzee@gmail.com"
    password = "rlebcifzblcrlenf"

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs="alphaanimefori99@gmail.com",
                            msg=f"The price of the item is ${price}")


