import logging
from logging.handlers import RotatingFileHandler
import os

# Optional: Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

log_file = 'logs/flask_server.log'

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3, mode='a'),  # append mode
        logging.StreamHandler()  # also print to console
    ]
)

logger = logging.getLogger(__name__)
logger.info("Starting the Flask app...")
