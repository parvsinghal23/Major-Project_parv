import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_info(product_name, product_price, product_ratings, product_reviews, recipient_email,product_link):
    # Email configuration
    sender_email = 'notificationapp27@gmail.com'  # Your Gmail email address
    sender_password = 'oevoyeyewlgpjgoz' # Your Gmail password
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Product Availability Notification'

    # Email content
    body = f"Product Name: {product_name}\nPrice: {product_price}\nRatings: {product_ratings}\nReviews: {product_reviews}\nproduct_link: {product_link}"
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
