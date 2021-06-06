from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep
from urllib.parse import quote
from sys import platform

options = Options()

f = open("mensagem.txt", "r")
message = f.read()
f.close()

print("##########################################################")
print('Mensagem que será enviada:')
print(message)
print("##########################################################")
message = quote(message)

numbers = []
f = open("numeros.txt", "r")
for line in f.read().splitlines():
	if line != "":
		numbers.append(line)
f.close()
total_number=len(numbers)
print("##########################################################")
print('\nNúmero de telefones encontrados: ' + str(total_number))
print("##########################################################")
print()
delay = 30

if platform == "win32":
	driver = webdriver.Chrome("drivers\\chromedriver.exe", options=options)
else:
	driver = webdriver.Chrome("./drivers/chromedriver", options=options)
print('Agora logue no WhatsApp!!')
driver.get('https://web.whatsapp.com')
input("Pressione ENTER quando estiver tudo OK.")
for idx, number in enumerate(numbers):
	if number == "":
		continue
	print('{}/{} => Enviando mensagem {}.'.format((idx+1), total_number, number))
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		driver.get(url)
		try:
			click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME , '_1E0Oz')))
		except (UnexpectedAlertPresentException, NoAlertPresentException) as e:
			print("alerta present")
			Alert(driver).accept()
		sleep(1)
		click_btn.click()
		sleep(3)
		print('Mensagem enviada com sucesso para o número: ' + number)
	except Exception as e:
		print('Falha ao enviar mensagem para o número: ' + number + str(e))
