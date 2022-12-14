from pydantic import BaseModel
import sys
sys.path.append("create_fact_models.py")

class Create_Fact(BaseModel):
    title: str
    city: str
    transport_ticket_total_value: float
    hotel_total_value: float
    remember: str