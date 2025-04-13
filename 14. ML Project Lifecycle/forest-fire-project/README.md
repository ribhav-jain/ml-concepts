# Flask Application

This section provides instructions to set up and run the Flask application for the project.

## Prerequisites

Ensure you have the following installed:

- Python (version 3.6 or higher)
- Required dependencies listed in `requirements.txt`

Install the dependencies using:

```
pip install -r requirements.txt
```

## Running the Flask Application

To start the Flask application, execute the following command in your terminal:

```
python app.py
```

## Accessing the Application

Once the application is running, you can access it by opening a web browser and navigating to:

```
http://127.0.0.1:5000/
```

If deploying to a remote server, replace `127.0.0.1` with your server's IP address or domain name:

```
http://{your_server_ip_or_domain}:5000/
```

## Notes

- Ensure port `5000` is open and not blocked by a firewall.
- For production deployment, consider using a WSGI server like Gunicorn or uWSGI.
