from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setup headless Chrome browser
options = Options()
options.headless = True

# Auto-install ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL of Syracuse men's basketball 2023-24 stats
url = "https://cuse.com/sports/mens-basketball/stats/2023-24"
driver.get(url)

# Wait for the page and table to load (adjust time if needed)
time.sleep(5)

# Get page source after full load
html = driver.page_source

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the main stats table (usually a <table> element)
table = soup.find("table")

# Get only the last header row from thead
thead_rows = table.find('thead').find_all('tr')
last_header = thead_rows[-1]
headers = [th.get_text(strip=True) for th in last_header.find_all('th')]


# Extract rows
rows = []
for tr in table.find('tbody').find_all('tr'):
    cells = [td.get_text(strip=True) for td in tr.find_all('td')]
    if len(cells) == len(headers):
        rows.append(cells)


# Create DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save to CSV
output_file = "syracuse_mbb_2023_24_stats.csv"
df.to_csv(output_file, index=False)

print(f"CSV saved as '{output_file}'")

# Quit browser
driver.quit()
