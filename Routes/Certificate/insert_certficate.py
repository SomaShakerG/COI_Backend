from fastapi import APIRouter, HTTPException
from app.dependencies import Mongo
from db.model.certificate import Certificate
from pymongo.errors import DuplicateKeyError
router = APIRouter()  # Use consistent name

@router.post("/certificates")
async def create_certificate(certificate: Certificate):
    db = Mongo.db  # Get db at runtime
    doc = certificate.dict()
    
    try:
        # Ensure unique index on producer email
        await db["certificates"].create_index("producer.email", unique=True)
        
        # Insert the document
        result = await db["certificates"].insert_one(doc)
        return {"inserted_id": str(result.inserted_id)}
    
    except DuplicateKeyError:
        # Raised if a unique constraint is violated
        raise HTTPException(status_code=400, detail="Producer email already exists")
    
    except Exception as e:
        # Catch any other errors
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/certificates")
async def list_certificates():
    db = Mongo.db  # Get db at runtime
    certificates = []
    cursor = db["certificates"].find({})
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        certificates.append(doc)
    return certificates
