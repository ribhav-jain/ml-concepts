# app.py
# Import the Flask class from the flask package
from flask import Flask

# Create an instance of the Flask class.
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses this to know where to look for resources like templates and static files.
app = Flask(__name__)


# Define a route for the root URL ('/') of the application.
# The @app.route() decorator tells Flask which URL should trigger our function.
@app.route("/")
def hello_world():
    return "Hello, Dockerized Flask World!"


# Check if the script is executed directly (not imported).
# This is common practice in Python scripts.
if __name__ == "__main__":
    # host='0.0.0.0' makes the server accessible from any IP address,
    # which is crucial for accessing it from outside the Docker container.
    # port=5000 specifies the port number the server will listen on.
    # debug=True enables Flask's debugger and auto-reloader, useful during development.
    app.run(host="0.0.0.0", port=5000, debug=True)
