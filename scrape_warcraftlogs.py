import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import lxml.html
from selenium import webdriver

url = 'https://www.warcraftlogs.com/reports/Rm7nJN1YpbkZFvBM'
response = requests.get(url)


# browser = webdriver.Firefox()
# browser.get(url) #navigate to the page
# innerHTML = browser.execute_script("return document.body.innerHTML")

# with open(f'test.html', 'w') as outfile:
#     outfile.write(innerHTML)


def extract_data_from_report(filename):
    html_report = open(filename, 'r')
    return BeautifulSoup(html_report, "html.parser")


def inner_html(element):
    """Returns the innter HTML of an element in BS4 as UTF-8 encoded Bytestring"""
    return element.text


def write_indexed_guilds_to_json():
    soup = extract_data_from_report('index.html')
    guild_rank = soup.find_all('td', {'class': 'guild-rank'})
    guild_name = soup.find_all('a', {'class': 'guild-href'})
    guild_names = []
    guild_ranks = []

    for r in guild_rank:
        guild_ranks.append(inner_html(r))

    for n in guild_name:
        guild_names.append(inner_html(n))

    guild_tuple = list(zip(guild_names, guild_ranks))

    with open(f'ranks.json', 'w') as outfile:
        outfile.write('[')
        outfile.write(f"{dict((y, x) for x, y in guild_tuple)}")
        outfile.write("]")

