from fastapi import FastAPI
import requests
import config

basic_app = FastAPI()

@basic_app.get("/")
def get_data():
    url =  f'http://{config.another_host}:{config.another_port}'
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        return {'ERROR':'ERROR'}

@basic_app.get("/another api/{api_request}")
def get_data(api_request : str):
    url =  f'http://{config.another_host}:{config.another_port}/{api_request}'
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        return {'ERROR':'ERROR'}