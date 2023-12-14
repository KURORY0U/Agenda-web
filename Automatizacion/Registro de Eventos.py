from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get("file:///C:/Users/Josue%20Mesa/Desktop/Cosas/Uni/9no%20Cuatrimestre/Prog%203/Agenda/index.html")

# Encontrar los elementos del formulario
nombre_input = driver.find_element("id", "nombre")
email_input = driver.find_element("id", "email")
celular_input = driver.find_element("id", "celular")
agregar_button = driver.find_element("xpath", "//button[contains(text(), 'Agregar')]")

# Ingresar información en el formulario
nombre_input.send_keys("Nombre de prueba")
email_input.send_keys("prueba@example.com")
celular_input.send_keys("123456789")
agregar_button.click()

# Esperar un momento para que se agregue el contacto
time.sleep(2)

# Verificar que el contacto se ha agregado correctamente
lista_contactos = driver.find_element("id", "listaContactos").text
assert "Nombre de prueba" in lista_contactos

# Cerrar el navegador
driver.quit()
