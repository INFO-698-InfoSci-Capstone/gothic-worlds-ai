from app import create_app
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read values from environment
host = os.getenv("FLASK_HOST", "127.0.0.1")
port = int(os.getenv("FLASK_PORT", 5000))
debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"

app = create_app()

if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)
