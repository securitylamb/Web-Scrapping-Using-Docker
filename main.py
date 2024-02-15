import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




#  adding Options here 
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
#  disabling memory for chrome 
chrome_options.add_argument('--disable-dev-shm-usage')
# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

# Define the URL you want to scrape
url = "website link here"

# Navigate to the URL
driver.get(url)

# Wait for some time to ensure the page is fully loaded
time.sleep(2)

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all headings with class 'elementor-heading-title'
headings = soup.find_all('h2', {'class': 'elementor-heading-title'})

# Extract and print text from headings
for heading in headings:
    print(heading.getText())

# Close the WebDriver
driver.quit()
