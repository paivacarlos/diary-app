from fastapi import FastAPI

from resource_app.post_resource import Create_Fact_Diary

app = FastAPI()

@app.get("/health")
async def root():
    return {"message": "We are online! :)"}

@app.post("/create-fact")
async def create_fact(new_fact: Create_Fact_Diary):
    response_body = {
        "message": "Fact Created with success!",
        "fact": new_fact
    }
    return response_body

