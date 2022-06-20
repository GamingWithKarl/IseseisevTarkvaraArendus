# Importib vajalikud asjad.
import requests as r
import json

# Kõik vajalik saatmiseks ning saamiseks.
service_plan_id = "BLANK" #Sisesta enda service id.#
access_token = "BLANK" #Sisesta enda access token#
from_ = "BLANK" #Sisesta enda sinch.com number.#
to_ = "BLANK" #Sisesta enda telefoni number kirja saamiseks.#

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


