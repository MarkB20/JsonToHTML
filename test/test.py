import io
import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.beautifulsoup import bs
from src.converter import converter

from deleteTest import deleteTest

import config
Input = os.path.dirname(__file__) + "/testFile"
Output = os.path.dirname(__file__) + "/outputTestFile"


class TestStringMethods(unittest.TestCase):

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
        bs(Output+"/test.html")
        # delete output contents

        deleteTest(Output)
        fake_file = "fake file for github"
        with open(f'{Output}/dummy.txt', 'w') as f:
            f.write(fake_file)
