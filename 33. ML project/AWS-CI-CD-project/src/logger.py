import logging
import os
from datetime import datetime

# Step 1: Generate a unique log filename with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Define the directory where logs will be stored
logs_dir = os.path.join(os.getcwd(), "logs")

# Step 3: Create the log directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Step 4: Build the full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Step 5: Configure logging with desired format and log level
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# Optional: You can also create a helper logger function for consistency
def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger with the specified module name.
    Use this in your modules: `logger = get_logger(__name__)`
    """
    return logging.getLogger(name)
