from fastapi import FastAPI

next_app = FastAPI()

@next_app.get('/')
def root():
    return {'content': 'root'}


@next_app.get("/get_data")
def get_data():
    return {'content': 'data'}