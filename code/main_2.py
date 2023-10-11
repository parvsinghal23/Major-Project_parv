import requests
from bs4 import BeautifulSoup
import time



def check_product_availability(product_url):
    # Define the API key and ScraperAPI endpoint
    api_key = '693020c26c7156542c1600e28dfedb35'
    scraperapi_endpoint = 'https://api.scraperapi.com/'

    # Define the ScraperAPI request payload
    payload = {
        'api_key': api_key,
        'url': product_url,
        'follow_redirect': True,
        'render': True,
        'retry_404': True,
        'autoparse': True
    }

    while True:
        # Make the API request
        response = requests.get(scraperapi_endpoint, params=payload)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Check if the product is available based on the presence of a "Buy Now" button
            buy_now_button = soup.find('button', {'class': '_2KpZ6l _2U9uOA _3v1-ww'})

            if buy_now_button:
                return "Product is available."
            else:
                return "Product is currently out of stock."
                time.sleep(2)  # Wait for 2 seconds before checking again
        else:
            return f"Failed to fetch data. Status code: {response.status_code}"
