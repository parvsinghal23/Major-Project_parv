import requests
from bs4 import BeautifulSoup

# Define the API key
api_key = '693020c26c7156542c1600e28dfedb35'

# Function to scrape and analyze the data for a given URL
def scrape_and_analyze(url):
    # Set up the API request payload
    payload = {
        'api_key': api_key,
        'url': url,
        'follow_redirect': True,
        'render': True,
        'retry_404': True,
        'autoparse': True
    }

    # Make the API request
    response = requests.get('https://api.scraperapi.com/', params=payload)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Check if the word "offer" is present in the page content
        keyword = 'offer'
        if keyword in soup.get_text().lower():
            print(f"Keyword '{keyword}' found on the page. An offer may be available for this product.")
        else:
            print(f"Keyword '{keyword}' not found. No offer detected for this product.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Get the user's input URL
user_url = input("Enter the URL of the product on Vijay Sales website: ")

# Call the function to scrape and analyze the data for the user-specified URL
scrape_and_analyze(user_url)