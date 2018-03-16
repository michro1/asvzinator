# ASVZINATOR

from bs4 import BeautifulSoup
import requests

BASE_URL = "https://schalter.asvz.ch"
SUB_URL = "/tn-mvc/Event/Lesson/Detail/"

RESERVATION_URL = "/tn-mvc/Registration/Reservation/MakeReservation/"

course_id = "608545"

cookies = {
    '.AspNet.ApplicationCookie': '',
    'ASP.NET_SessionId': '',
    'FedAuth': '',
    'FedAuth1': '',
    '__RequestVerificationToken_L3RuLW12Yw2': '',
    '_shibsession': '',
    'jwt_token': ''
    
}

page = requests.get(BASE_URL + SUB_URL + course_id, cookies=cookies)
soup = BeautifulSoup(page.content, 'html.parser')

form = soup.select('form[action='+RESERVATION_URL + course_id + '] input')


verification_token = form[0]['value']

payload = {'__RequestVerificationToken': verification_token}

headers = {'Referer': 'https://schalter.asvz.ch/tn-mvc/Event/Lesson/Detail/608545'}

r = requests.post(BASE_URL + RESERVATION_URL + course_id, data=payload, headers=headers)

print(r.text)
