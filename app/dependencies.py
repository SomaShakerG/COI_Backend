from db.connect  import  Mongo
async def get_db():
    return Mongo.db  # returns the same db instance everywhere
