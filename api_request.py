from api_config import *
import requests


def getMethodJsonFromApi(url):

    headers = {"api_key": getApiKey(), "api_id": getApiId()}

    return requests.get(url, headers=headers).json()


def postMethodJsonFromApi(url):

    headers = {"api_key": getApiKey(), "api_id": getApiId()}

    return requests.post(url, headers=headers).json()