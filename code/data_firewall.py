import pandas as pd

# Load the Excel file containing student data
data = pd.read_excel('students.xlsx')

# Define a function to search for a student by SAP ID and return their name
def get_student_name(sap_id):
    student_data = data.loc[data['SAP ID'] == sap_id]
    if len(student_data) > 0:
        return student_data.iloc[0, 1] # return the name in the next column
    else:
        return 'Student not found'

import pandas as pd

# Load the Excel file containing student data
data = pd.read_excel('students.xlsx')

# Define a function to search for a student by SAP ID and return their name
def get_student_name(sap_id):
    student_data = data.loc[data['SAP ID'] == sap_id]
    if len(student_data) > 0:
        return student_data.iloc[0, 1] # return the name in the next column
    else:
        return 'Student not found'

# Flask integration to create a web application
from flask import Flask, request

app = Flask(__name__)

@app.route('/search_student', methods=['GET'])
def search_student():
    sap_id = request.args.get('sap_id')
    return get_student_name(sap_id)

if __name__ == '__main__':
    app.run()
