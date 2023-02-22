from fastapi import APIRouter
from database.database import database

router = APIRouter()


@router.get("/")
async def list_one_fact(db=database, id_fact=str):
    response_body = {"message": "Nothing is here"}

    for fact in range(len(db)):
        data_from_db = f"{db[fact]['id']}"
        id_fact_from_request = f'{id_fact}'
        if data_from_db == id_fact_from_request:
            response_body = {'fact:': db[fact]['data']}
            break

    return response_body
