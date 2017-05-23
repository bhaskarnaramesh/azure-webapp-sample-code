from datetime import timedelta
from datetime import datetime

import requests


class AzureAuthClient(object):
    def __init__(self, client_secret):
        self.client_secret = client_secret
        self.token = None
        self.reuse_token_until = None

    def get_access_token(self):
        if (self.token is None) or (datetime.utcnow() > self.reuse_token_until):
            token_service_url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'

            request_headers = {'Ocp-Apim-Subscription-Key': self.client_secret}

            response = requests.post(token_service_url, headers=request_headers)
            response.raise_for_status()

            self.token = response.content
            self.reuse_token_until = datetime.utcnow() + timedelta(minutes=5)

        return self.token