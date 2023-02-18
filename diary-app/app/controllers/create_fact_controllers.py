import uuid

from fastapi import APIRouter

from models.create_fact_models import Create_Fact
from database.database import database

router = APIRouter()

db = database


@router.post("/")
async def create_fact(new_fact: Create_Fact):
    db.append({
        'id': uuid.uuid4(),
        'data': new_fact
    })
    response_body = db[-1]
    return response_body
