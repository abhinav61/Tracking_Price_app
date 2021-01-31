import requests
from bs4 import BeautifulSoup
import smtplib


URL = "https://www.amazon.in/CAMRO-Brown-Casual-Outdoor-Shoes/dp/B07PB41HDD/ref=sr_1_3_sspa?crid=HY838EUS8ZL9&keywords=casual+shoes+for+mens+under+1000&qid=1578581994&sprefix=casual+%2Caps%2C277&sr=8-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFMQzhSMDVHNlRJTEMmZW5jcnlwdGVkSWQ9QTA1MDUzOTgxNjFaMlpDWEtJQVVWJmVuY3J5cHRlZEFkSWQ9QTAwMjAyMjczT0tFRk5XT1QxVllDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
def check_price():

	
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id= "productTitle").get_text()
    price = soup.find(id = "priceblock_saleprice").get_text()
    

    print(title.strip())
    print(price.strip())


   
check_price()

'''
def send_mail():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('abhinavk806@gmail.com', 'mmzuflhsvtlvlvhm')

	subject = 'Hey Price Fell down!'
    
     
    

    server.sendmail(
    	'abhinavk806@gmail.com',
    	'abhijeetsugam@gmail.com',
    	
    )

    print("email has been sent")
    server.quit()

check_price()
'''