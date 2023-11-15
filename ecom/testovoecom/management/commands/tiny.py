from django.core.management.base import BaseCommand
from tinydb import TinyDB, Query
import json

'''
email
телефон
дата
текст.
'''


class Command(BaseCommand):
    # db = TinyDB('db.json')

    def handle(self, *args, **options):
        form_templates = [{"name": "UserForm",
                           "lead_email": "email",
                           "user_phone": "phone"
                           },

                          {"name": "OrderForm",
                           "lead_email": "email",
                           "order_date": "date"
                           },

                          {
            "name": "EmailTextForm",
            "lead_email": "email",
            "data": "text"
        },
            {
            "name": "TelephoneDateForm",
            "user_phone": "phone",
            "order_date": "date"
        },
            {
            "name": "TelephoneTextForm",
            "user_phone": "phone",
            "data": "text"
        },
            {
            "name": "DateTextForm",
            "order_date": "date",
            "data": "text"
        }
        ]
        db = TinyDB("db.json")
        for data in form_templates:
            db.insert(data)
