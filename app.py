from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define route for the root URL
@app.route('/')
def hello_world():
    return 'Teshs Great Application'

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)