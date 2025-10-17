from fastapi import APIRouter, Depends
from app.dependencies import get_db


router = APIRouter()

@router.post("/")
async def create_employee(user: dict, db=Depends(get_db)):
    result = await db["users"].insert_one(user)
    return {"inserted_id": str(result.inserted_id)}

@router.get("/")
async def list_employees(db=Depends(get_db)):
    users = []
    cursor = db["users"].find({})
    async for document in cursor:
        document["_id"] = str(document["_id"])
        users.append(document)
    return users
