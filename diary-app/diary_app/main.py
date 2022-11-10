from fastapi import FastAPI

from resource_app.post_resource import Create_Fact_Diary

app = FastAPI()

database = []

@app.get("/health")
async def root():
    return {"message": "We are online! :)"}

@app.post("/create-fact")
async def create_fact(new_fact: Create_Fact_Diary):
    database.append(new_fact)
    response_body = new_fact
    return response_body