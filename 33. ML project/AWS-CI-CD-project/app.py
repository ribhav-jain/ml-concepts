"""
app.py

Main Flask application for Student Exam Performance Prediction.

Routes:
- "/"          : Renders the index (landing) page.
- "/predictdata": Handles GET (form) and POST (prediction) requests.
"""

from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask application
application = Flask(__name__)
app = application  # Alias for flexibility


@app.route("/")
def index():
    """
    Renders the index page (landing page).
    """
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    """
    Handles form submission and renders prediction result.

    - GET: Render the form page.
    - POST: Process input, run prediction, and render result.
    """
    if request.method == "GET":
        return render_template("home.html")

    try:
        # Extract and validate form data
        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(
                request.form.get("reading_score")
            ),  # Fixed correct mapping
            writing_score=float(
                request.form.get("writing_score")
            ),  # Fixed correct mapping
        )

        # Convert input to DataFrame
        pred_df = data.get_data_as_data_frame()
        print("[DEBUG] Input DataFrame:", pred_df)

        # Perform prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Render result page with prediction
        return render_template("home.html", results=results[0])

    except Exception as e:
        # If there's an error, you can return a friendly message
        print(f"[ERROR] Prediction failed: {e}")
        return render_template(
            "home.html", results="Prediction Failed! Please check inputs."
        )


if __name__ == "__main__":
    # Run the app on host 0.0.0.0 and port 8080 (for Docker/cloud environments)
    app.run(host="0.0.0.0", port=8080, debug=True)
