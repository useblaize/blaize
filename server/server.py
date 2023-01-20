from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
async def get_root():
    return {"generate": random.randint(1, 1000)}