import os
import unittest
from os import path

from selenium import webdriver
from selenium.webdriver.common.by import By

import config
from deleteTest import deleteTest
from src.converter import converter
from src.copyStyle import copyStyle

Input = os.path.dirname(__file__) + "/testFile"
Output = os.path.dirname(__file__) + "/outputTestFile"
cl_path = config.Input
htmlr_path = config.Output
stylesheet = os.path.dirname(__file__) + "/outputTestFile/stylesheet.css"


class TestStringMethods(unittest.TestCase):

    def test_FilePath(self):
        self.assertEqual(path.isdir(cl_path), True)
        self.assertEqual(path.isdir(htmlr_path), True)

    def test_stylesheet(self):
        copyStyle(Output)
        self.assertEqual(path.isfile(stylesheet), True)
        deleteTest(Output)

    def test_converter(self):
        # run the converter with a test file and test output file
        converter(Input, Output)
        # opens the local html file in the firefox browser
        browser = webdriver.Firefox()
        browser.get(r"file://"+Output+"/test.html")
        # try to find the word apple in the output of the json file
        apple = browser.find_element(By.CSS_SELECTOR, "body > table:nth-child(1) > tbody:nth"
                                                      "-child(1) > tr:nth-child(1) > td:nth-child(2)")
        # asserts if the word apple is found
        self.assertEqual(apple.text, "Apple")
        # quits the browser
        browser.quit()
        # delete output contents
        deleteTest(Output)

    def test_soup(self):
        # run the converter with a test file and test output file
        converter(Input, Output)
        # opens the local html file in the firefox browser
        browser = webdriver.Firefox()
        browser.get(r"file://" + Output + "/test.html")
        # goes to the path to find the link tag
        link = browser.find_element(By.CSS_SELECTOR, "head>link:nth-child(1)")
        # asserts if the link tag was found
        self.assertEqual('link', link.tag_name)
        # quits the browser
        browser.quit()
        # deletes the output so that it can be fairly tested again
        deleteTest(Output)
