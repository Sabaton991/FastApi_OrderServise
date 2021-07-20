from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def base_route():
    return {'data': 'Hello'}
