import requests
from bs4 import BeautifulSoup
import time
from send_email import send_info


# Define the ScraperAPI request payload
def check_product_availability(product_url, recipient_email):
    api_key = '08787347edb086d69d60b4425f0508fe'
    scraperapi_endpoint = 'https://api.scraperapi.com/'

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
                print("Product is available, details has send to you email!!")
                # flash('Product is available, details has send to you email!!')

                # Scrape additional details
                product_name = soup.find('span', {'class': 'B_NuCI'}).text
                product_price = get_product_price(soup)
                product_ratings = get_product_ratings(soup)
                product_reviews = get_product_reviews(soup)

                send_info(product_name, product_price, product_ratings, product_reviews, recipient_email,product_url)
                break
            else:
                print("Product is currently out of stock. Checking again in 2 seconds...")
                # flash('Product is currently out of stock. Checking again in 2 seconds...')
                break
                 # Wait for 1 seconds before checking again
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            # flash('Failed to fetch data.')
            break

# Function to extract product price
def get_product_price(soup):
    price_element = soup.find('div', {'class': '_30jeq3'})
    if price_element:
        return price_element.text
    else:
        return "Price not available"

# Function to extract product ratings
def get_product_ratings(soup):
    ratings_element = soup.find('div', {'class': '_3LWZlK'})
    if ratings_element:
        return ratings_element.text
    else:
        return "Ratings not available"

# Function to extract product reviews
def get_product_reviews(soup):
    reviews_element = soup.find('span', {'class': '_2_R_DZ'})
    if reviews_element:
        return reviews_element.text
    else:
        return "Reviews not available"


# # Check if the user wants to automate availability checking and receive notifications
# automate_checking = input("Automate availability checking and receive email notifications? (yes/no): ").lower()
# if automate_checking == "yes" or automate_checking == "Yes" or  automate_checking == "YES" or automate_checking == "Y" or automate_checking == "y":
#     check_product_availability(product_url, recipient_email)
# else:
#     print("You chose not to automate availability checking.")
