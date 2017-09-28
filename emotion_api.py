import http.client
import json
import urllib.error
import urllib.parse
import urllib.request

import config

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': config.sub_key,
}


def get_emotion(img):

    params = urllib.parse.urlencode({
    })

    body = "{ 'url': '" + img + "' }"

    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()

    data = json.loads(response.read().decode())

    return data
