import pandas as pd
import requests

EXCEL_PATH = 'Mobile Data.xlsx'

import os
TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']
TWILIO_CALL_API = f'https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Calls.json'
AUTH = (TWILIO_SID, TWILIO_TOKEN)
FROM_NUMBER = '+14143480238'  # Twilio number

df = pd.read_excel(EXCEL_PATH)

for index, row in df.iterrows():
    if row['Call Status'] != 'Completed':
        to_number = str(int(float(row['Mobile Number']))).strip()
        payload = {
            'From': FROM_NUMBER,
            'To': f'+91{to_number}',
            'Url': 'https://autocalldesk.onrender.com/twiml'
        }
        response = requests.post(TWILIO_CALL_API, data=payload, auth=AUTH)
        print(f"Calling {to_number}: {response.status_code}")
