from fastapi import APIRouter, HTTPException
from database.database import database
from models.create_fact_models import Create_Fact

router = APIRouter()


@router.put("/")
async def update_fact(data_update_fact: Create_Fact, db=database, id_fact=str):
    response_body = None
    controller = False

    if len(db) == 0:
        response_body = {"message": "Database is empty"}
    else:
        for fact in range(len(db)):
            data_from_db = str(db[fact]['id'])
            id_fact_from_request = str(id_fact)
            if data_from_db == id_fact_from_request:
                db.pop(fact)
                db.append({
                    'id': id_fact_from_request,
                    'data': data_update_fact
                })
                response_body = {'updated fact:': db[fact]}
                controller = True
                break

    if len(db) > 0 and controller is False:
        raise HTTPException(status_code=400, detail="This ID is not exist!")

    return response_body
