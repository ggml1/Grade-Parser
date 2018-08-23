from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials
import gspread

def get_all_names():
    scope = ['https://spreadsheets.google.com/feeds' + ' ' + 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open("Notas - Alunos").sheet1

    grades_sheet = sheet.get_all_records()

    students_data = list()
    sheet_line = 1
    
    for student in grades_sheet:
        students_data.append((sheet_line, student['Nome'], student[' Login']))
        sheet_line = sheet_line + 1

    students_data.pop();

    return students_data

def main():
    students = list()
    students = get_all_names()

    for student_info in students:
        print(student_info)

if __name__ == "__main__":
    main()