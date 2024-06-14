from app import app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV') == 'development')
