from fastapi import APIRouter

from controllers import create_fact_controllers
from controllers import list_all_facts_controllers
from controllers import list_one_fact_controllers
from controllers import update_fact_controller

router = APIRouter()

router.include_router(create_fact_controllers.router, prefix="/create-fact")
router.include_router(list_all_facts_controllers.router, prefix="/list-all-facts")
router.include_router(list_one_fact_controllers.router, prefix="/list-one-fact/{id_fact}")
router.include_router(update_fact_controller.router, prefix="/update-fact/{id_fact}")
