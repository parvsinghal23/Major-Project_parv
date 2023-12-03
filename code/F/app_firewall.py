import re
from flask import Flask, request, Response, render_template, redirect, url_for , session

# Create an instance of the Flask class and set the name of the application
app = Flask(__name__)

# Define a function to check if the user has answered at least one firewall security question
def has_answered_security_question():
    enable_firewall1 = request.form.get('enable_firewall1')
    enable_firewall2 = request.form.get('enable_firewall2')
    return enable_firewall1 is not None or enable_firewall2 is not None or request.method == 'GET'

# Define a Flask route for the root URL of the web application
@app.route('/')
def route():
        return redirect('/login')

@app.route('/index', methods=['GET','POST'])
def index():
    # If the request method is POST (i.e. the user has submitted data)
    if request.method == 'POST':
        # Check if the user has answered at least one firewall security question and if the answer is yes or no
        if not has_answered_security_question() or (request.form.get('question') == 'yes' or request.form.get('question') == 'no'):
            return "Please answer at least one security question with a yes or no response to access the input box."

        # Get the submitted data from the form
        data = request.form['data']

        # Check if the user wants to enable the first firewall security
        enable_firewall1 = request.form.get('enable_firewall1')
        if enable_firewall1 == 'yes':
            # Import the security_scan function from the first firewall_security module
            from firewall_security import security_scan

            # Call the security_scan function to check for potential security issues
            if security_scan(data):
                # If the data passes the security scan, return a success message
                return "Data submitted successfully!"
            else:
                # If potential security issues are found, return an error message
                return "Security scan detected potentially malicious content in your data."
        if enable_firewall1 == 'no':
            return "Data submitted successfully!"

        # Check if the user wants to enable the second firewall security
        enable_firewall2 = request.form.get('enable_firewall2')
        if enable_firewall2 == 'yes':
            # Import the security_scan function from the second firewall_security module
            from firewall_security import security_scan

            # Call the security_scan function to check for potential security issues
            if security_scan(data):
                # If the data passes the security scan, return a success message
                return "Data submitted successfully!"
            else:
                # If potential security issues are found, return an error message
                return "Security scan detected potentially malicious content in your data."
        
        if enable_firewall2 == 'no':
            return "Data submitted successfully!" 
    # If neither firewall security is enabled, redirect the user to the login page
    else:
        return render_template('index.html')

# Define a Flask route for the login page
# Define a Flask route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the request method is POST (i.e. the user has submitted login data)
    if request.method == 'POST':
        # Get the submitted username and password from the form
        return render_template('index.html')
    # If the request method is not POST, return an HTML form asking for login credentials
    else:
        return render_template('login.html')

@app.route('/get_student_name', methods=['GET'])
def get_student_name():
    sap_id = request.args.get('sap_id')
    return get_student_name(sap_id)

if __name__ == '__main__':
    # Start the Flask application and set it to run in debug mode
    app.run(host='localhost', port=8080, debug=True)