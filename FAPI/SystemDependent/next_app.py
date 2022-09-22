from fastapi import FastAPI

next_app = FastAPI()

@next_app.get('/')
def root():
    return {'Project':'Draft'}


@next_app.get("/get_data")
def get_data():
    return {'Project':'Draft'}