import os
from twilio.rest import Clients

load_dotenv()

accountSID = os.getenv('SID')
authToken = os.getenv('TOKEN')

