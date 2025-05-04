# Dockerfile
# Use an official Python runtime as a parent image
# Using slim for a smaller image size
FROM python:3.11-slim

# Set environment variables
# Prevents Python from buffering stdout and stderr
# This is useful for logging, as it ensures that logs are printed immediately
# instead of being buffered, which can cause delays in log output.
ENV PYTHONUNBUFFERED=1

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
# All subsequent commands (COPY, RUN, CMD) will be relative to this path
WORKDIR /app

# Can have multiple run but only 1 CMD
# Install system dependencies
# Example: For projects needing PostgreSQL client libs (psycopg2) or build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
# Copying requirements first allows Docker to cache the dependency installation layer
# if requirements.txt hasn't changed, speeding up subsequent builds.
# Doing this after copying only requirements.txt allows Docker to cache this layer. If you change your application code but not the requirements, Docker reuses this layer, speeding up builds significantly.
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
# --no-cache-dir: Disables the pip cache, reducing image size.
# -r requirements.txt: Tells pip to install packages from the given requirements file.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code (e.g., app.py) into the container at /app
COPY . .

# Make port 5000 available to the world outside this container
# This doesn't actually publish the port, it's more like documentation.
# Publishing happens when you run the container (e.g., with docker run -p or docker-compose).
EXPOSE 5000

# Define environment variables (optional)
# Example: Setting Flask environment to development (enables debug mode if app.run has debug=True)
ENV FLASK_ENV=development
ENV FLASK_APP=app.py

# Migrations (python manage.py migrate) should generally not be run in the Dockerfile's RUN command. They modify the database state, which shouldn't be part of the immutable image build process.

# Command to run the application when the container launches
# Uses 'flask run' which leverages the FLASK_APP and FLASK_ENV variables.
# --host=0.0.0.0 is crucial to make the app accessible from outside the container.
CMD ["flask", "run", "--host=0.0.0.0"]
#Similar to cmd minor difference, only the last ENTRYPOINT instruction is effective
# ENTRYPOINT ["python3", "app.py"]
