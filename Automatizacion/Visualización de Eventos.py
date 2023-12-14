from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get("file:///C:/Users/Josue%20Mesa/Desktop/Cosas/Uni/9no%20Cuatrimestre/Prog%203/Agenda/index.html") 

try:
    # Encontrar los elementos del formulario y el botón de agregar
    nombre_input = driver.find_element("id", "nombre")
    email_input = driver.find_element("id", "email")
    celular_input = driver.find_element("id", "celular")
    agregar_button = driver.find_element("xpath", "//button[contains(text(), 'Agregar')]")

    # Hacer clic en el botón de agregar sin completar los campos
    agregar_button.click()

    # Esperar un momento para que aparezca la alerta
    time.sleep(2)

    # Verificar que se muestre la alerta de llenado de campos
    alerta = driver.switch_to.alert
    assert "Por favor, complete todos los campos" in alerta.text

    # Aceptar la alerta
    alerta.accept()

    # Mostrar mensaje de éxito
    print("Operación exitosa: Se mostró la alerta de llenado de campos correctamente.")

except Exception as e:
    # Mostrar mensaje de error en caso de cualquier excepción
    print(f"Error: {e}")

finally:
    # Cerrar el navegador
    driver.quit()

