import os
import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time

# Configuration
ASIN = "B077PZKNDH" # Example ASIN
# ESIN = "386065059274" #example ESIN
RECEIVER_EMAIL = "parvsinghal23@gmail.com"
GMAIL_USERNAME = os.environ.get('GMAIL_USERNAME')  # Use environment variables
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')

MAX_RETRIES = 2  # Maximum number of retries

def amazon_check_availability(amazon_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    
    for _ in range(MAX_RETRIES):
        try:
            response = requests.get(amazon_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            availability_element = soup.select_one('div#availabilityInsideBuyBox_feature_div span.a-size-medium.a-color-success')
            
            if availability_element:
                availability_text = availability_element.get_text().strip()
                if "In Stock" in availability_text:
                    availability = "In Stock"
                else:
                    availability = "Not in stock"
            else:
                availability = "Availability information not found"

            return availability
        except requests.exceptions.RequestException:
            print("Retrying...")
            time.sleep(2)  # Add a delay before retrying
    
    return "Unable to determine availability"





# def ebay_check_availability(ebay_url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    
#     for _ in range(MAX_RETRIES):
#         try:
#             response = requests.get(ebay_url, headers=headers)
#             response.raise_for_status()
#             soup = BeautifulSoup(response.content, 'html.parser')
#               # Update the element locator based on the actual HTML structure of eBay's product page
#             availability_element = soup.select_one('span#qtySubTxt span.rcnt')

#             if availability_element:
#                 availability_text = availability_element.get_text().strip()
#                 if "In Stock" in availability_text:
#                     availability = "In Stock"
#                 else:
#                     availability = "Not in stock"
#             else:
#                 availability = "Availability information not found"

#             return availability
#         except requests.exceptions.RequestException:
#             print("Retrying eBay request...")
#             time.sleep(2)  # Add a delay before retrying
    
#     return "Unable to determine eBay availability"


def send_email(subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(GMAIL_USERNAME,GMAIL_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(GMAIL_USERNAME, RECEIVER_EMAIL, message)

def track_availability():
    
    amazon_url = f"https://www.amazon.com/dp/{ASIN}"    
    print(f"Checking availability for ASIN: {ASIN}")
    # ebay_url = f"https://www.ebay.com/itm/{ESIN}"
    # print(f"Checking availability for ebay ESIN: {ESIN}")
    
    try:
        amazon_availability = amazon_check_availability(amazon_url)
       # ebay_availability = ebay_check_availability(ebay_url)
        
        print(f"Amazon Availability: {amazon_availability}")
        # print(f"eBay Availability: {ebay_availability}")
        
        if "In Stock" in amazon_availability:         # or "In Stock" in ebay_availability:
            subject = f"Product {ASIN} is Available!"
            body = f"The product with ASIN {ASIN} is now in stock.\n\nCheck it out on Amazon: {amazon_url}" # \nCheck it out on eBay: {ebay_url}"
            send_email(subject, body)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("Product Availability Checker Started")
    schedule.every(0.2).minutes.do(track_availability)  # Check every 1 minutes

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()






# #using amazon 
# url = f"https://www.amazon.com/dp/{ASIN}"
# print(f"Checking availability for ASIN: {ASIN}")

# def track_availability():

#     try:
#         availability = amazon_check_availability(url)
#         print(f"Availability: {availability}")
#         if "In stock" in availability:
#             subject = f"Product {ASIN} is Available!"
#             body = f"The product with ASIN {ASIN} is now in stock.\n\nCheck it out on Amazon: {url}"
#             send_email(subject, body)
#     except Exception as e:
#         print(f"An error occurred: {e}")