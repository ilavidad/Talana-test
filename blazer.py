import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class productPurchase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")

        
    def buy(self):

        #CREATE user
        Singup = self.driver.find_element(by="id", value= "signin2")
        Singup.click()

        Singup = self.driver.find_element(by="id", value= "sign-username")
        Singup.click()

        formName = self.driver.find_element(by="id", value= "sign-username")
        #Ingresar ejemplo nombre usuario
        formName.send_keys("pr5")

        Singup = self.driver.find_element(by="id", value= "sign-password")
        Singup.click()

        formName = self.driver.find_element(by="id", value= "sign-password")
        #Ingresar ejemplo contraseña usuario
        formName.send_keys("123")
        time.sleep(3)

        ButtonSingup = self.driver.find_element(by="xpath", value='//*[@id="signInModal"]/div/div/div[3]/button[2]')
        ButtonSingup.click()
        time.sleep(3)

        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(5)


        #LOG IN user
        Login = self.driver.find_element(by="xpath", value='//*[@id="login2"]')
        Login.click()
        time.sleep(3)

        userName = self.driver.find_element(by="id", value="loginusername")
        userName.click()

        FormName = self.driver.find_element(by="id", value="loginusername")
        #Ingresar ejemplo nombre usuario
        FormName.send_keys("pr5")
        

        userPass = self.driver.find_element(by="id", value="loginpassword")
        userPass.click()

        FormPass = self.driver.find_element(by="id", value="loginpassword")
        #Ingresar ejemplo contraseña usuario
        FormPass.send_keys("123")



        ButtonLogin = self.driver.find_element(by="xpath", value='//*[@id="logInModal"]/div/div/div[3]/button[2]')
        ButtonLogin.click()
        time.sleep(10)



        #ADD laptop a cart
        ItemLaptops = self.driver.find_element("link text", "Laptops")
        ItemLaptops.click()
        time.sleep(5)

        addLaptop = self.driver.find_element(by="xpath", value="//a[@href='prod.html?idp_=11']")    
        addLaptop.click()
        time.sleep(5)

        addCart = self.driver.find_element(by="css selector", value=".btn-success.btn-lg")
        addCart.click()
        time.sleep(5)

        alert = self.driver.switch_to.alert
        alert.accept()

        Home= self.driver.find_element(by="xpath", value="//a[@href='index.html']")
        Home.click()
        time.sleep(5)

        Cart = self.driver.find_element(by="xpath", value="//a[@href='cart.html']")
        Cart.click()
        time.sleep(5)

        Home= self.driver.find_element(by="xpath", value="//a[@href='index.html']")
        Home.click()
        time.sleep(5)


        #ADD phone a cart
        ItemPhones = self.driver.find_element("link text", "Phones")
        ItemPhones.click()
        time.sleep(3)

        addPhone = self.driver.find_element(by="xpath", value="//a[@href='prod.html?idp_=7']")
        addPhone.click()
        time.sleep(3)

        addCart = self.driver.find_element(by="css selector", value=".btn-success.btn-lg")
        addCart.click()
        time.sleep(3)

        alert = self.driver.switch_to.alert
        alert.accept()

        Home= self.driver.find_element(by="xpath", value="//a[@href='index.html']")
        Home.click()
        time.sleep(5)

        Cart = self.driver.find_element(by="xpath", value="//a[@href='cart.html']")
        Cart.click()
        time.sleep(5)

        Home= self.driver.find_element(by="xpath", value="//a[@href='index.html']")
        Home.click()
        time.sleep(5)


        #ADD monitor a cart

        ItemMonitors = self.driver.find_element("link text", "Monitors")
        ItemMonitors.click()
        time.sleep(3)

        addMonitor = self.driver.find_element(by="xpath", value="//a[@href='prod.html?idp_=10']")
        addMonitor.click()
        time.sleep(3)

        addCart = self.driver.find_element(by="css selector", value=".btn-success.btn-lg")
        addCart.click()
        time.sleep(3)

        alert = self.driver.switch_to.alert
        alert.accept()


        Cart = self.driver.find_element(by="xpath", value="//a[@href='cart.html']")
        Cart.click()
        time.sleep(5)

        #SHOPPING cart

        placeOrder = self.driver.find_element(by="xpath", value ='//*[@id="page-wrapper"]/div/div[2]/button')
        placeOrder.click()
        time.sleep(3)

        OrderName = self.driver.find_element(by="id", value="name")
        OrderName.click()
        time.sleep(3)

        FormplaceName = self.driver.find_element(by="id", value="name")
        FormplaceName.send_keys("prueba1")

        OrderCountry = self.driver.find_element(by="id", value="country")
        OrderCountry.click()

        FormplaceCountry = self.driver.find_element(by="id", value="country")
        FormplaceCountry.send_keys("Chile")

        OrderCity= self.driver.find_element(by="id", value="city")
        OrderCity.click()

        FormplaceCity = self.driver.find_element(by="id", value="city")
        FormplaceCity.send_keys("Santiago")

        OrderCreditcard = self.driver.find_element(by="id", value="card")
        OrderCreditcard.click()

        FromplaceCreditcard = self.driver.find_element(by="id", value="card")
        FromplaceCreditcard.send_keys("787815")

        OrderMonth = self.driver.find_element(by="id", value="month")
        OrderMonth.click()

        FromplaceMonth = self.driver.find_element(by="id", value="month")
        FromplaceMonth.send_keys("08")

        OrderYear = self.driver.find_element(by="id", value="year")
        OrderYear.click()

        FromplaceYear = self.driver.find_element(by="id", value="year")
        FromplaceYear.send_keys("2036")


        Purchase = self.driver.find_element(by="xpath", value ='//*[@id="orderModal"]/div/div/div[3]/button[2]')
        Purchase.click()
        time.sleep(10)

        elemento= self.driver.find_element(by="xpath", value='/html/body/div[10]/p/br[2]')
        elemento_esperado = "787815"
        texto_obtenido = FromplaceCreditcard.get_attribute("value")
        assert texto_obtenido == elemento_esperado, f"El texto ingresado '{texto_obtenido}' no coincide con el texto esperado '{elemento_esperado}'."


        confirm = Purchase = self.driver.find_element(by="xpath", value ='/html/body/div[10]/div[7]/div/button')
        confirm.click()
        
        def tearDown(self):
            self.driver.quit()



if __name__ == "__main__":
    unittest.main()



