from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import os
from backend.chat_router import router as chat_router
from backend.memory_router import router as memory_router
from backend.file_upload import router as upload_router

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/backend.log'),
        logging.StreamHandler()
    ]
)

app = FastAPI(title="XiaoChenGuang AI Soul System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api", tags=["Chat"])
app.include_router(memory_router, prefix="/api", tags=["Memory"])
app.include_router(upload_router, prefix="/api", tags=["Upload"])

@app.get("/")
async def root():
    return {"message": "XiaoChenGuang AI Soul System API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="localhost", port=port)
