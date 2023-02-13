import io
import os
import unittest
from os.path import exists
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.beautifulsoup import bs
from src.converter import converter
from src.copyStyle import copyStyle
from deleteTest import deleteTest
import config

Input = os.path.dirname(__file__) + "/testFile"
Output = os.path.dirname(__file__) + "/outputTestFile"

cl_path = exists(config.Input)
htmlr_path = exists(config.Output)
stylesheet = os.path.dirname(__file__) + "/outputTestFile/stylesheet.css"


class TestStringMethods(unittest.TestCase):

    def stylesheet_exists(self):
        self.assertEquals((str(cl_path), cl_path.is_file()), (str(cl_path), True))
        self.assertEquals((str(htmlr_path), htmlr_path.is_file()), (str(htmlr_path), True))

    def stylesheet_exists(self):
        copyStyle(Output)
        self.assertEquals((str(stylesheet), stylesheet.is_file()), (str(stylesheet), True))
        deleteTest(Output)

    def test_coverter(self):
        # run the converter with a test file and test output file
        converter(Input, Output)
        # opens the local html file in the firefox browser
        browser = webdriver.Firefox()
        browser.get(r"file://"+Output+"/test.html")
        # try to find the word apple in the output of the json file
        apple = browser.find_element(By.CSS_SELECTOR,"body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)")
        # asserts if the word apple is found
        self.assertEqual(apple.text, "Apple")
        browser.quit()
        # delete output contents

        deleteTest(Output)

