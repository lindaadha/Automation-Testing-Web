import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://barru.pythonanywhere.com/daftar")
        self.driver.maximize_window
        
    def test_a_success_login(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com")
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys("testerjago")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/h2"))
            )
        finally:
            time.sleep(3)
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
            respon_welcome = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
            respon_berhasil = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
            self.assertEqual(respon_welcome, "Welcome tester jago")
            self.assertEqual(respon_berhasil, "Anda Berhasil Login")
            time.sleep(5)

    def test_b_failed_login_email_not_registered(self):
        driver = self.driver
        # driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("tester.ganteng@jumawa.com")
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys("testerjago")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/h2"))
            )
        finally:
            time.sleep(3)
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
            respon_welcome = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
            respon_berhasil = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
            self.assertIn("not found",respon_welcome)
            self.assertIn("Salah", respon_berhasil)
            self.assertEqual(respon_welcome, "User\'s not found")
            self.assertEqual(respon_berhasil, "Email atau Password Anda Salah")
            time.sleep(5)
    
    def test_c_failed_email_not_valid(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com")
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys("12345")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/h2"))
            )
        finally:
            time.sleep(3)
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
            respon_welcome = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
            respon_berhasil = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
            self.assertEqual(respon_welcome, "User\'s not found")
            self.assertEqual(respon_berhasil, "Email atau Password Anda Salah")
            time.sleep(5)

    def test_d_failed_login_password_false(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("testerjagoqa.com")
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys("12345")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/h2"))
            )
        finally:
            time.sleep(3)
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
            respon_welcome = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
            respon_berhasil = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
            self.assertEqual(respon_welcome, "Email tidak valid")
            self.assertEqual(respon_berhasil, "Cek kembali email anda")
            time.sleep(5)

    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()