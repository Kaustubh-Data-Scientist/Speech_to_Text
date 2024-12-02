import logging
import os
from datetime import datetime

# Define log directory and file name
LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example usage:
# logging.info("This is an info message")
# logging.error("This is an error message")
