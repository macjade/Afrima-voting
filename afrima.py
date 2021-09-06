import csv
import random
import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Pythonafrima(unittest.TestCase):
    seq = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    number = '1234567890'
    names = ['Luciana Goodman', 'Regan Baird', 'Destiny Allen', 'Thomas Snow', 'Zackary Decker', 'Gracie Larson', 'Rylee Hensley', 'Mohammed Flowers', 'Amira Cannon', 'Kamari Hogan',
             'Kinsley Barnett', 'Jazmyn Richmond', 'Alena Knapp', 'Anna Lozano', 'Carl Jordan', 'Annabelle Parks', 'Madison Mccall',
             'Angela Gates', 'Pamela Dunn', 'Steven Clayton', 'Alayna Bartlett', 'Alex Faulkner', 'Savanah Mercado', 'Natasha Peters',
             'Harper Singleton', 'Azaria Glass', 'Eva Mcknight', 'Axel Jacobson', 'Anne Fuentes', 'Devin Davila', 'Dayana Montgomery',
             'Samson Kaiser', 'Kristen Chase', 'Jacey Hanson', 'Stella Pitts', 'Ahmad Farrell', 'Laurel Castro', 'Crystal Fleming',
             'Isaias Glenn', 'Wayne Gates', 'Salvatore Sampson', 'Jaidyn Washington', 'Arturo Harmon', 'Iris Rowland', 'Patience Owens',
             'Kody Curtis', 'Desmond Kidd', 'Lee Stout', 'Thalia Fernandez', 'Gwendolyn Mann', 'Harper Carter', 'Selina Gomez',
             'Audrey Whitney', 'Jordan Sawyer', 'Messiah Mcgrath', 'Kolton Dillon', 'Finn Mcpherson', 'Cory Allen', 'Taniyah Farley',
             'Noelle Elliott', 'Elisabeth Livingston', 'Vanessa Evans']

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\PrayingReconciliatio\\Desktop\\selenium\\chromedriver.exe")

    def test_vote(self):
        driver = self.driver
        driver.maximize_window()
        csv_array = []

        for i in self.names:
            with open('old.csv', 'r') as disreport:

                reader = csv.reader(disreport, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                count = sum(1 for row in reader)
                print(count)
                if count == 0:
                    pass
                else:
                    for r_row in reader:
                        csv_array.append(r_row)

            if i in csv_array:
                continue
            else:
                mail = i.split(' ')
                e_mail = mail[0].lower()

                driver.get("https://www.mailf5.com/")
                driver.find_element_by_id('inbox-id').click()
                driver.find_element_by_xpath('//*[@id="inbox-id"]/input').send_keys(str(e_mail))
                driver.find_element_by_xpath('//*[@id="inbox-id"]/button[1]').click()

                driver.get('https://afrima.org/6thAfrimavoting/register')
                driver.find_element_by_name('name').send_keys(str(i))
                driver.find_element_by_name('phone').send_keys('+23481' + str(random.randint(1, 100000000)))
                driver.find_element_by_name('email').send_keys(str(e_mail)+'@mailf5.com')
                driver.find_element_by_xpath('//*[@name="country"]/option[text()="Nigeria"]').click()
                driver.find_element_by_name('password').send_keys('1234567890')
                driver.find_element_by_name('c_password').send_keys('1234567890')
                driver.find_element_by_class_name('btn').click()

                driver.implicitly_wait(20)
                time.sleep(10)

                driver.get("https://www.mailf5.com/")
                driver.implicitly_wait(6)
                driver.find_element_by_xpath('//*[starts-with(@id, "mr_") and contains(@id, "4")]').click()
                driver.implicitly_wait(10)
                driver.find_element_by_partial_link_text('https://afrima.org/6thAfrimavoting/verify-me/').click()

                driver.get("https://afrima.org/6thAfrimavoting/getaccess")
                driver.find_element_by_name('email').send_keys(str(e_mail)+'@mailf5.com')
                driver.find_element_by_name('password').send_keys('1234567890')
                driver.find_element_by_class_name('btn').click()

                driver.implicitly_wait(15)
                # west africa category
                driver.get("https://afrima.org/6thAfrimavoting/home/best-female-artiste-in-western-africa")
                driver.find_element_by_xpath('//*[@eid="67"]').click()

                driver.implicitly_wait(20)
                # inspirational music
                driver.get("https://afrima.org/6thAfrimavoting/home/best-female-artiste-duo-or-group-in-african-inspirational-music")
                driver.find_element_by_xpath('//*[@eid="251"]').click()

                driver.implicitly_wait(20)
                # inspirational music
                driver.get("https://afrima.org/6thAfrimavoting/home/songwriter-of-the-year-in-africa")
                driver.find_element_by_xpath('//*[@eid="313"]').click()

                driver.implicitly_wait(20)
                time.sleep(10)
                driver.get("https://afrima.org/6thAfrimavoting/profile")
                sa_name = ''.join(random.choice(self.seq) for l in range(4))
                driver.save_screenshot(str(sa_name)+'.png')

                with open('old.csv', 'w') as reportcsv:
                    filewriter = csv.writer(reportcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(i)

                driver.get("https://afrima.org/6thAfrimavoting/log/out")



if __name__ == "__main__":
    unittest.main()