import os
from dotenv import load_dotenv
from upstox_api.api import Upstox

load_dotenv()
API_KEY = os.getenv("API_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
u = Upstox(API_KEY, ACCESS_TOKEN)
print(u.get_profile()) # get profile
