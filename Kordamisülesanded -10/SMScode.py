# Importib vajalikud asjad.
import requests as r
import json

# Kõik vajalik saatmiseks ning saamiseks.
service_plan_id = "b6ff9fe4021147fbb1a87647764cf50f" #Sisesta enda service id.#
access_token = "e15ad7d6fd5f4d3cb76938643e29edb7" #Sisesta enda access token#
from_ = "447520652179" #Sisesta enda sinch.com number.#
to_ = "37256946313" #Sisesta enda telefoni number kirja saamiseks.#

# Headerid authorizationiks.
headers = {
    "Authorization":f"Bearer {access_token}",
    "Content-Type":"application/json"
}

# Saatmiseks vajalik sisu numbritega ja kirjaga "Hello World!"
payload = {
    "from":from_,
    "to":[to_],
    "body":"Hello from the world of Python! ;)"
}

# Saadab kirja telefoni peale kasutades sinch api'd.
r.post(
    f'https://sms.api.sinch.com/xms/v1/{service_plan_id}/batches',
    headers = headers,
    data = json.dumps(payload)
)


# Dokumentatsioon
# Kood kasutab antud variable'id (nagu telefoni numberid ja service ning access tokeneid) sõnumite edastamiseks.
# Koodi sisse saab määrata sõnumi ning selle saata saaja telefoninumbrile.

# Kasutusala saab olla sellel automatiseeritud sõnumitel (nt pakikoodid ja authincation koodide) saatmisel.
# Arendada saaks sõnumit ise, aga oleneb kasutusalal (nt saab pakikoodid genereerida koodi sees ning pärast sellega pakiukse lahti teha.


