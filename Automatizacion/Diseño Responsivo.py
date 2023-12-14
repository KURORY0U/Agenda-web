from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configuración del navegador
driver = webdriver.Chrome()

# Acceder a la página web
driver.get("file:///C:/Users/Josue%20Mesa/Desktop/Cosas/Uni/9no%20Cuatrimestre/Prog%203/Agenda/index.html")  # Reemplaza con la ruta de tu archivo

# Maximizar la ventana para simular una pantalla grande
driver.maximize_window()
time.sleep(2)  # Esperar a que la página se cargue completamente (puedes ajustar el tiempo según sea necesario)

# Tomar una captura de pantalla o realizar otras verificaciones según tus necesidades

# Redimensionar la ventana para simular una pantalla pequeña (por ejemplo, un dispositivo móvil)
driver.set_window_size(360, 640)  # Ajusta el tamaño según tus necesidades
time.sleep(2)  # Esperar a que la página se ajuste al nuevo tamaño (puedes ajustar el tiempo según sea necesario)

# Tomar otra captura de pantalla o realizar otras verificaciones según tus necesidades

# Cerrar el navegador
driver.quit()
