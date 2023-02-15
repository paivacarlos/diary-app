from fastapi import FastAPI

from routes import router

app = FastAPI()


@app.get("/health")
async def root():
    return {"message": "We are online! :)"}


app.include_router(router, prefix="")
