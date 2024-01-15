from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello_world() -> object:
    return {'Message': 'Hello World'}
