import threading
import requests
from bs4 import BeautifulSoup
import time

# BeautifulSoup:
# BeautifulSoup is a Python library for parsing HTML and XML documents.
# It allows developers to navigate, search, and modify HTML or XML data easily.
# It is commonly used in web scraping to extract data from web pages.
# How BeautifulSoup Works
# Parsing: BeautifulSoup parses raw HTML data into a structured tree format.
# Navigating: You can traverse the parsed document's nodes and find specific tags or content.
# Searching: You can search by tag name, CSS class, or other attributes.
# Extracting Data: After parsing the page, you can extract the required content.


# Function to fetch content and parse the HTML
def fetch_and_parse(url):
    try:
        print(f"Fetching URL: {url}")
        # Request data from the URL
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Parsing content from: {url}")
            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            # Extract the title of the page
            title_tag = soup.find("title")
            if title_tag:
                print(f"Title of {url}: {title_tag.text}")
            else:
                print(f"No title found for {url}")
        else:
            print(f"Failed to fetch {url}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while fetching or parsing {url}: {e}")


# URLs to scrape
urls = [
    "https://docs.djangoproject.com/en/5.1/topics/logging/",
    "https://docs.djangoproject.com/en/5.1/",
    "https://docs.djangoproject.com/en/5.1/ref/middleware/#security-middleware",
]

# Create threads for concurrent fetching and parsing
threads = []
start_time = time.time()

for url in urls:
    t = threading.Thread(target=fetch_and_parse, args=(url,))
    threads.append(t)
    t.start()  # Start the thread

# Wait for all threads to complete
for t in threads:
    t.join()

end_time = time.time()

print(
    f"Total execution time with multithreading and BeautifulSoup: {end_time - start_time} seconds"
)

# Fetching URL: https://docs.djangoproject.com/en/5.1/topics/logging/
# Fetching URL: https://docs.djangoproject.com/en/5.1/
# Fetching URL: https://docs.djangoproject.com/en/5.1/ref/middleware/#security-middleware
# Parsing content from: https://docs.djangoproject.com/en/5.1/
# Parsing content from: https://docs.djangoproject.com/en/5.1/topics/logging/
# Parsing content from: https://docs.djangoproject.com/en/5.1/ref/middleware/#security-middleware
# Title of https://docs.djangoproject.com/en/5.1/: Django documentation | Django documentation | DjangoTitle of https://docs.djangoproject.com/en/5.1/topics/logging/: Logging | Django documentation | Django

# Title of https://docs.djangoproject.com/en/5.1/ref/middleware/#security-middleware: Middleware | Django documentation | Django
# Total execution time with multithreading and BeautifulSoup: 0.4237189292907715 seconds
