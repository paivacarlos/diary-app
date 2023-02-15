from fastapi import APIRouter

from controllers import create_fact_controllers
from controllers import list_all_facts_controllers

router = APIRouter()

router.include_router(create_fact_controllers.router, prefix="/create-fact")
router.include_router(list_all_facts_controllers.router, prefix="/list-all-facts")
