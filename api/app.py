from fastapi import FastAPI
from routes.students import router
from config.db import client

app = FastAPI(title='Rest API', description='Students REST API with FastAPI & MongoDB.')

app.include_router(router)

@app.on_event("shutdown")
def close_connection():
    client.close()
    print("MongoDB connection closed.")
