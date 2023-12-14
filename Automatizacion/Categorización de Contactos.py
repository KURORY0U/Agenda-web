import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCategorizacionContactos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///C:/Users/Josue%20Mesa/Desktop/Cosas/Uni/9no%20Cuatrimestre/Prog%203/Agenda/index.html") 
        
    def test_agregar_categoria_a_contacto(self):
        # Aquí realizas la prueba de agregar una categoría a un contacto
        # Puedes utilizar los métodos de Selenium para interactuar con la interfaz de usuario
        pass

    def test_editar_categorias_de_contacto(self):
        # Aquí realizas la prueba de editar las categorías de un contacto
        # Puedes utilizar los métodos de Selenium para interactuar con la interfaz de usuario
        pass

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
