from fastapi import FastAPI

app = FastAPI(

    title="Course Management API",

    version="1.0"

)


@app.get("/")

async def home():

    return {

        "message": "API running"

    }
