from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# @app.get("/")
# def home():
#     return {"HEllo": "FastAPI"}


# @app.get("/contact/{contact_id}")
# def contact_details(contact_id: int, page: Optional[int] = 1):
#     if page:
#         return {'contact_id': contact_id, 'page': page}
#     return {'contact_id': contact_id}

class Contact(BaseModel):
    contact_id:int
    first_name:str
    last_name:str
    user_name:str
    password:str

@app.post('/contact')
async def create_contact(contact: Contact):
    return contact