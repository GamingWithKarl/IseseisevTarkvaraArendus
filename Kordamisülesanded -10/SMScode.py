# Importib vajalikud asjad.
import requests as r
import json

# Kõik vajalik saatmiseks ning saamiseks.
service_plan_id = "BLANK" #Sisesta enda service id.#
access_token = "BLANK" #Sisesta enda access token#
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
    "body":"Hello world!"
}

# Saadab kirja telefoni peale kasutades sinch api'd.
r.post(
    f'https://sms.api.sinch.com/xms/v1/{service_plan_id}/batches',
    headers = headers,
    data = json.dumps(payload)
)