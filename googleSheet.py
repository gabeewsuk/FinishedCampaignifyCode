from oauth2client.service_account import ServiceAccountCredentials
import gspread
from gspread_dataframe import set_with_dataframe


def sendToGoogleSheets(df):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/spreadsheets']

    #Generate a json file by using service account auth in google developer console
    '''
    Link: https://console.developers.google.com/
    1) Enable API Access for a Project if you haven’t done it yet.
    2) Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
    3) Fill out the form
    4) Click “Create” and “Done”.
    5) Press “Manage service accounts” above Service Accounts.
    6) Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.
    7) Select JSON key type and press “Create”.
    '''
    creds = ServiceAccountCredentials.from_json_keyfile_name('mod.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1lF1hghCqq90sez6mujjzqBbKuxL9Fb7SgYCR6rB2kX4/edit#gid=0").sheet1

    data = sheet.get_all_records()

    #sheet.update_cell(1, 1, "You made it") #Write this message in first row and first column

    #print(data)

    set_with_dataframe(sheet, df)