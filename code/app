from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code',methods=['POST'])
def run_code():
    email = request.args.get('email')
    username = request.args.get('username')
    # Place the provided code module here
    
    # ...
    return "Code executed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
