from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from tinydb import TinyDB
from tinydb import Query
import re
query = Query()
db = TinyDB("db.json")

# Create your views here.
#^(0?[1-9]|[12][0-9]|3[01])[-](0?[1-9]|1[012])[-]\d{4}$
def get_form(request: HttpRequest):
    context = {
        "lead_email": "email",
        "user_phone": "phone",
        "order_date": "date",
        "data": "text"
    }
    value = request.GET.dict().keys()
    f1 = []
    for v in value:
        if context.get(v) != None:
            # print(re.search(r'^((\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,13}$',request.GET.dict().get(v)))
            if v == 'user_phone' and re.search(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,12}$',request.GET.dict().get(v))==None:
                return HttpResponse(f"<h2>Невалидный номер телефона</h2>")
            if v == 'lead_email' and re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', request.GET.dict().get(v)) == None:
                return HttpResponse(f"<h2>Невалидный email</h2>")
            if v == 'order_date' and (re.search(r'^(((0[1-9]|[12][0-9]|30)[-/]?(0[13-9]|1[012])|31[-/]?(0[13578]|1[02])|(0[1-9]|1[0-9]|2[0-8])[-/]?02)[-/]?[0-9]{4}|29[-/]?02[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$', request.GET.dict().get(v)) 
                                    or re.search(r'^([0-9]{4}[-/]?((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00)[-/]?02[-/]?29)$', request.GET.dict().get(v)))== None:
                return HttpResponse(f"<h2>Невалидная дата</h2>")
            f1.append(v)
    if len(f1) >= 2:
        result = db.get((query[f1[0]] == context[f1[0]]) & (query[f1[1]] == context[f1[1]]))
        if result != None:
            return HttpResponse(f"{result['name']}")
    else:
        return render(request, 'testovoecom/main.html', {'result':context})
    # else:
    #     result = {}
    #     for index in range(len(f1)):
    #         ser = db.search(query[f1[index]] == context[f1[index]])
    #         for x in ser:
    #             result[x.get('name')] = x
    #     print(result)
    #     return render(request, 'testovoecom/main.html', {'result':result})
    return render(request, 'testovoecom/main.html', {})
