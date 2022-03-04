from api_config import *
import requests


def getMethodJsonFromApi(url):
    # API with header
    # headers = {"api_key": getApiKey(), "api_id": getApiId()}

    return requests.get(url).json()


def postMethodJsonFromApi(url):
    # headers = {"api_key": getApiKey(), "api_id": getApiId()}

    return requests.post(url).json()
