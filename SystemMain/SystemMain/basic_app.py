from fastapi import FastAPI
import requests
import os

basic_app = FastAPI()

@basic_app.get("/")
def get_data():
    url = os.getenv("URL")
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        return {'ERROR': 'ERROR'}

@basic_app.get("/do_something")
def get_data():
    url = f'{os.getenv("URL")}/get_data'
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        return {'ERROR': result.status_code,
            'RESULT': result}