from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup

options = Options()
options.headless = True  # run headless so no browser window opens

# This line automatically downloads & manages ChromeDriver
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.espn.com/mens-college-basketball/team/stats/_/id/183/season/2024"
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')

headers = [th.text for th in table.find_all('th')]

rows = []
for tr in table.find_all('tr')[1:]:
    cells = [td.text.strip() for td in tr.find_all('td')]
    if cells:
        rows.append(cells)

df = pd.DataFrame(rows, columns=headers)
df.to_csv('syracuse_basketball_2024_stats.csv', index=False)

print("CSV saved as syracuse_basketball_2024_stats.csv")

driver.quit()
