import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2022-10-21',authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    frenchTranslate = language_translator.translate(text=englishText,model_id='en-fr').get_result()
    frenchText = frenchTranslate.get("translations")[0].get("translation")
    return frenchText

def frenchToEnglish(frenchText):
    englishTranslate = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    englishText = englishTranslate.get("translations")[0].get("translation")
    return englishText