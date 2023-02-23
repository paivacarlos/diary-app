from fastapi import APIRouter, HTTPException
from database.database import database

router = APIRouter()


@router.get("/")
async def list_one_fact(db=database, id_fact=str):
    response_body = None
    controller = False

    if len(db) == 0:
        response_body = {"message": "Database is empty"}
    else:
        for fact in range(len(db)):
            data_from_db = str(db[fact]['id'])
            id_fact_from_request = str(id_fact)
            if data_from_db == id_fact_from_request:
                response_body = {'fact:': db[fact]['data']}
                controller = True
                break

    if len(db) > 0 and controller is False:
        raise HTTPException(status_code=400, detail="This ID is not exist!")

    return response_body
