from fastapi import APIRouter

router = APIRouter()

database = [{"message": "Not database online"}]


@router.get("/")
async def list_all_facts():
    response_body = database
    return response_body
