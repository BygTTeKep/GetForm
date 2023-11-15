from django.test import TestCase
from tinydb import TinyDB, Query
from django.urls import reverse
import requests

# Create your tests here.

class GetFormTestCase(TestCase):
    def setUp(self) -> None:
        query = Query()
        db = TinyDB("db.json")
    def test_get_form(self):
        testCase = [
                {
                    'name': 'TelephoneDateForm',
                    'url': 'user_phone=+79230085043&order_date=2023-08-23',
                },
                {
                    'name': 'OrderForm',
                    'url': 'lead_email=example@example.com&order_date=2023-08-23',
                },
                {
                    'name': 'EmailTextForm',
                    'url': 'lead_email=example@example.com&data=text',
                },
                {
                    'name': 'TelephoneTextForm',
                    'url': 'user_phone=+79230085043&data=text',
                },
                {
                    'name': 'DateTextForm',
                    'url': 'order_date=2023-08-23&data=text',
                },
                {
                    'name': 'UserForm',
                    'url': 'lead_email=example@example.com&user_phone=+79230085043',
                },
                {
                    'name': 'OrderForm',
                    'url': 'lead_email=example@example.com&order_date=2023-08-23',
                },
                {
                    'name': 'EmailTextForm',
                    'url': 'lead_email=example@example.com&data=text',
                },
                {
                    'name': 'TelephoneDateForm',
                    'url': 'user_phone=+79230085043&order_date=2023-08-23',
                },
                {
                    'name': 'TelephoneTextForm',
                    'url': 'user_phone=+79230085043&data=text',
                },
                {
                    'name': 'DateTextForm',
                    'url': 'order_date=2023-08-23&data=text',
                },
        ]
        # print(testCase['user_phone'])
        for tc in testCase:
            print(tc['name'])
            res = requests.get('http://127.0.0.1:8000/get_form?'+tc['url'])
            self.assertEqual(res.text, tc['name'])