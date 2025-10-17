from fastapi import FastAPI
import uvicorn
import main
from db.connect import Mongo
from Routes.Certificate.insert_certficate import router as certificate_route
# from Routes.user.create import router as employees
app = FastAPI()

# Connect and disconnect events
@app.on_event("startup")
async def startup_event():
     await Mongo.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await Mongo.close()
app.include_router(certificate_route, prefix="/api")
if __name__ =="__main__":
 uvicorn.run(app,host="0.0.0.0",port=8000,reload=True,)

