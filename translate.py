from xml.etree import ElementTree
from auth import AzureAuthClient
import requests


def GetTextAndTranslate(finalToken):
    toLangCode = 'ko'
    textToTranslate = " "

    textToTranslate = input("Type the text that you want to translate:  ")

    # Call to Microsoft Translator Service
    headers = {"Authorization ": finalToken}
    translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate,
                                                                                                   toLangCode)

    translationData = requests.get(translateUrl, headers=headers)
    # parse xml return values
    translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
    # display translation
    print(translation.text)


if __name__ == "__main__":
    client_secret = 'aa8af3404b854b7f80a6f988fe179f1b'
    auth_client = AzureAuthClient(client_secret)
    bearer_token = b'Bearer ' + auth_client.get_access_token()
    GetTextAndTranslate(bearer_token)