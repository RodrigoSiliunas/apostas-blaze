import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
CHANNEL_ID = int(os.environ.get('CHANNEL_ID'))
