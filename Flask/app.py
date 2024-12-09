from flask import Flask, redirect, render_template, request, jsonify, abort, url_for

# Command to run Flask application:
# For Windows: set FLASK_APP=app.py
# For macOS/Linux: export FLASK_APP=app.py
# Then run the command: flask run

# Initialize a new Flask application
# 1. Flask: The class used to create the app instance.
# 2. __name__: A special variable that helps Flask determine the root path of the application.
# 3. app: The variable that holds the instance of the Flask app, used to define routes and handle requests.
app = Flask(__name__)


# Home route that renders the main index template
@app.route("/")
def home():
    # Render the HTML template for the home page
    return render_template("index.html")


# Simple welcome route
@app.route("/welcome")
def welcome():
    # Return a simple HTML response
    return "<html><h1>Welcome to the Flask app</h1></html>"


"""
# Jinja2 Templating Basics
1. **Expressions**:
   - {{ ... }}: Used to print variables or expressions in HTML.
     Example: {{ username }} will render the value of the variable `username`.

2. **Control Structures**:
   - {% ... %}: Used for control flow statements like loops and conditions.
     Example:
     - For Loop:
       {% for item in list %}
           <li>{{ item }}</li>
       {% endfor %}
     - Conditional Statement:
       {% if user.is_admin %}
           <p>Welcome, Admin!</p>
       {% else %}
           <p>Welcome, User!</p>
       {% endif %}

3. **Comments**:
   - {# ... #}: Used for comments that will not be rendered in the output HTML.
     Example: {# This is a comment and will not appear in the final HTML #}

4. **Filters**:
   - Filters can modify variables. They are applied using the pipe (|) symbol.
     Example: {{ message|capitalize }} will capitalize the first letter of `message`.

5. **Macros**:
   - Macros allow you to define reusable pieces of template code.
     Example:
     ```
     {% macro input(name, value='') %}
         <input type="text" name="{{ name }}" value="{{ value }}">
     {% endmacro %}
     ```

6. **Blocks**:
   - Used in template inheritance to define sections that can be overridden in child templates.
     Example:
     ```
     {% block content %}
         <h1>Default Content</h1>
     {% endblock %}
     ```

7. **Inheritance**:
   - Jinja allows templates to inherit from a base template to promote reusability.
     Example:
     ```
     {% extends "base.html" %}
     ```
"""


# Route to render a user profile with dynamic data
@app.route("/user/<username>")
def user_profile(username):
    # Pass the username variable to the user.html template
    return render_template("user.html", username=username)


# Route to serve static files (like CSS, JavaScript, images)
@app.route("/static-file-example")
def static_file_example():
    # Render an HTML template that demonstrates static file usage
    return render_template("static_example.html")


# Example of handling GET requests with query parameters
@app.route("/search")
def search():
    query = request.args.get("query")  # Get the 'query' parameter from the URL
    return f"Search results for: {query}"


# Feedback route to handle feedback submissions
@app.route("/feedback", methods=["POST", "GET"])
def feedback():
    average_rating = 0  # Initialize variable to store average rating
    if request.method == "POST":
        # Retrieve ratings from the form using request.form
        quality = float(request.form["quality"])
        value = float(request.form["value"])
        service = float(request.form["service"])

        # Calculate average rating from the retrieved values
        average_rating = (quality + value + service) / 3

        # Redirect to the result page with the average rating
        return redirect(url_for("feedback_result", rating=average_rating))
    else:
        # Render the feedback form for GET requests
        return render_template("feedback_form.html")


# Route to display feedback results
@app.route("/feedback_result")
def feedback_result():
    rating = request.args.get("rating", type=float)  # Get rating from query parameters
    return render_template("feedback_result.html", rating=rating)


# Example of handling POST requests
@app.route("/submit", methods=["POST"])
def submit():
    # Get data from the form submission
    data = request.form["data"]
    # Respond with JSON indicating successful data reception
    return jsonify({"message": "Data received!", "data": data})


# Error handling: 404 Not Found error
@app.errorhandler(404)
def page_not_found(e):
    # Render a custom 404 error page
    return render_template("404.html"), 404


# Error handling: 500 Internal Server Error
@app.errorhandler(500)
def internal_error(e):
    # Render a custom 500 error page
    return render_template("500.html"), 500


# Example API route (GET method) to return JSON data
@app.route("/api/data", methods=["GET"])
def get_data():
    example_data = {"key1": "value1", "key2": "value2"}
    # Return JSON response
    return jsonify(example_data)


# Example API route (POST method) to accept JSON data
@app.route("/api/data", methods=["POST"])
def post_data():
    content = request.json  # Get JSON data from the request body
    # Respond with the received content
    return jsonify({"message": "Data received!", "received": content})


# Middleware function to log incoming requests
@app.before_request
def log_request():
    # Log the method and path of each incoming request
    print(f"Incoming request: {request.method} {request.path}")


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)  # Set debug=True for development, auto-reload on code changes
