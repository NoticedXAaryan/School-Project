# THIS PROGRAM HAS BEEN REPURPUSED FROM MY GITHUB (NOTICEDXAARYAN)
# This was originally made as an internship project but now i have reused it.

# Importing necacery library
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSelectorException
import pandas as pd
import time

# Function to open the browser and navigate to the given URL
def open_browser(url):
    try:
        # Set up the webdriver
        driver = webdriver.Chrome()
        driver.get(url)
        return driver
    except Exception as e:
        print(f"Error opening the browser: {e}")
        return None
    

# Opening the website
url = "https://www.azquotes.com/"
driver = open_browser(url)

# Clicking on "Top Quotes" button 
top_quotes_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
top_quotes_button.click()

# Waiting
time.sleep(3)

# creating a empty list
quotes_list = []

# Scraping 1000 quotes ;)
while len(quotes_list) < 1000:

    time.sleep(2)  # waiting

    # using beautifulscoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Find the quotes
    quotes = soup.find_all('div', class_='wrap-block')
    
    for quote in quotes:
        if len(quotes_list) >= 1000:  # Stop if we already have 1000 quotes
            break
        try:
            # Scraping the quote text
            quote_text = quote.find('a', class_='title').text.strip()

            # Scraping the author
            author = quote.find('div', class_='author').text.strip()
            
            # Scraping the type of quote
            type_of_quote = quote.find('div', class_='tags').text.strip()

            # Storing the data in a list of dictionary
            quotes_list.append({
                'Quote': quote_text,
                'Author': author,
                'Type/Genre': type_of_quote
            })

        # Skip if any required data is not found   
        except AttributeError:
            continue 

    # Try to click the "Next" button for pagination
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'Next →')])[1]"))
        )
        next_button.click()

    # Break out of the loop if error occurs   
    except Exception:
        break 

# Convert the scraped data into a DataFrame
df = pd.DataFrame(quotes_list)

# Showing the DataFrame with no index :^] 
print( df.head(5) )
print( df.tail(5) )

# Save the data to a CSV file
df.to_csv('quotes.csv', index=False)

# Close the driver after scraping
driver.quit()