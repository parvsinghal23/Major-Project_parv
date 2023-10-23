import requests
from bs4 import BeautifulSoup
import time
from send_email import send_info

# Define the ScraperAPI request payload
def check_product_availability(product_url, recipient_email):
<<<<<<< HEAD
    api_key = 'kkkkkkkkkkkkkkkkkkkkk'
=======
    api_key = 'ff66fb14fa09f0e634e916608b107d60'
>>>>>>> 3c0c5d0566d46a7ebb7a5ab99350cd2ed7733841
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

                # Scrape additional details
                product_name = soup.find('span', {'class': 'B_NuCI'}).text
                product_price = get_product_price(soup)
                product_ratings = get_product_ratings(soup)
                product_reviews = get_product_reviews(soup)

<<<<<<< HEAD
                send_info(product_name, product_price, product_ratings, product_reviews, recipient_email)
=======
                send_info(product_name, product_price, product_ratings, product_reviews, recipient_email,product_url)
>>>>>>> 3c0c5d0566d46a7ebb7a5ab99350cd2ed7733841
                break
            else:
                print("Product is currently out of stock. Checking again in 2 seconds...")
                time.sleep(1)  # Wait for 1 seconds before checking again
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            break

# Function to extract product price
def get_product_price(soup):
    price_element = soup.find('div', {'class': '_30jeq3'})
    if price_element:
        return price_element.text
<<<<<<< HEAD
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

product_url = input("Enter the Flipkart product URL: ")
recipient_email = input("Enter your email address: ")

# Check if the user wants to automate availability checking and receive notifications
automate_checking = input("Automate availability checking and receive email notifications? (yes/no): ").lower()
if automate_checking == "yes" or automate_checking == "Yes" or  automate_checking == "YES" or automate_checking == "Y" or automate_checking == "y":
    check_product_availability(product_url, recipient_email)
else:
    print("You chose not to automate availability checking.")















































# import requests
# from bs4 import BeautifulSoup
# import time

# # Define the API key and ScraperAPI endpoint
# api_key = '693020c26c7156542c1600e28dfedb35'
# scraperapi_endpoint = 'https://api.scraperapi.com/'

# # Prompt the user to enter the product URL
# product_url = input("Enter the Flipkart product URL: ")

# # Define the ScraperAPI request payload
# payload = {
#     'api_key': api_key,
#     'url': product_url,
#     'follow_redirect': True,
#     'render': True,
#     'retry_404': True,
#     'autoparse': True
# }

# while True:
#     # Make the API request
#     response = requests.get(scraperapi_endpoint, params=payload)

#     if response.status_code == 200:
#         # Parse the HTML content
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Check if the product is available based on the presence of a "Buy Now" button
#         buy_now_button = soup.find('button', {'class': '_2KpZ6l _2U9uOA _3v1-ww'})
        
#         if buy_now_button:
#             print("Product is available.")
#             break
#         else:
#             print("Product is currently out of stock. Checking again in 2 seconds...")
#             time.sleep(2)  # Wait for 2 seconds before checking again
#     else:
#         print(f"Failed to fetch data. Status code: {response.status_code}")
#         break

    
    
    
    
    
# import requests
# from bs4 import BeautifulSoup

# # Define the API key and request payload
# api_key = '693020c26c7156542c1600e28dfedb35'
# url = 'https://www.flipkart.com/asus-zenfone-max-pro-m1-grey-32-gb/p/itmf4hg4z55waayn?pid=MOBF3A8UMME3H2BZ&lid=LSTMOBF3A8UMME3H2BZPJPNUD'

# payload = {
#     'api_key': api_key,
#     'url': url,
#     'follow_redirect': True,
#     'render': True,
#     'retry_404': True,
#     'autoparse': True
# }

# # Make the API request
# response = requests.get('https://api.scraperapi.com/', params=payload)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Print the parsed HTML content
# print(soup)
=======
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

product_url = input("Enter the Flipkart product URL: ")
recipient_email = request.form['email']

# Check if the user wants to automate availability checking and receive notifications
automate_checking = input("Automate availability checking and receive email notifications? (yes/no): ").lower()
if automate_checking == "yes" or automate_checking == "Yes" or  automate_checking == "YES" or automate_checking == "Y" or automate_checking == "y":
    check_product_availability(product_url, recipient_email)
else:
    print("You chose not to automate availability checking.")
>>>>>>> 3c0c5d0566d46a7ebb7a5ab99350cd2ed7733841
