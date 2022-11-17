from fastapi import APIRouter

from models.create_fact_models import Create_Fact

router = APIRouter()

database = []


@router.post("/")
async def create_fact(new_fact: Create_Fact):
    database.append(new_fact)
    response_body = new_fact
    return response_body
