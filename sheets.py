import gspread
import google.auth
from datetime import datetime 
from datetime import date
from os import environ

DEFAULT_SCOPES =[
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials, project = google.auth.default(
    scopes=DEFAULT_SCOPES
)

gc= gspread.Client(auth=credentials)

sh = gc.open_by_key(environ['SHEET_ID'])


def get_channel_id():
    worksheet = sh.get_worksheet(0)
    
    try:
        val = worksheet.get('B1').first()
        return int(val)
    except:
        return None

def get_question():
    worksheet = sh.get_worksheet(0)
    try:
        val = worksheet.get('B2').first()
        return str(val)
    except:
        return None

def record_answer(author,answer):
    answer_sheet = sh.worksheet("Answers")

    question=get_question()

    datetime_now=datetime.now().isoformat()

    # answer_sheet.update('A2:E2', [[question,author,answer,datetime_now]])
    answer_sheet.append_row([question,author,answer,datetime_now])


