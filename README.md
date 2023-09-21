# Toolkit to download slides from a website

This is a simple Python tool to download Files from a certain website. Feel free to add more function if you need!

## An example to use:

python download_from_website.py --website "https://csci1410-2022.vercel.app/" --pattern 'a[href^="/files/lectures/"]'

## Requirements:

import argparse
import requests
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver

## Arguments:

parser.add_argument('--website', '-w', required=True, help='Website URL to scrape.')
parser.add_argument('--pattern', '-p', required=True, help='CSS selector pattern to match links.')
parser.add_argument('--time', '-t', help = "Time you want the website to wait.",default = 3000)
