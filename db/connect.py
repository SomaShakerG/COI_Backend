from motor.motor_asyncio import AsyncIOMotorClient

class Mongo:
    client = None
    db = None

    @classmethod
    async def connect(cls, uri="mongodb://localhost:27017", db_name="testdb"):
        cls.client = AsyncIOMotorClient(uri)
        cls.db = cls.client[db_name]
        print("✅ Connected to MongoDB")

    @classmethod
    async def close(cls):
        if cls.client:
            cls.client.close()
            print("❌ MongoDB connection closed")
