from pydantic import BaseModel

class Create_Fact(BaseModel):
    title: str
    city: str
    transport_ticket_total_value: float
    hotel_total_value: float
    remember: str