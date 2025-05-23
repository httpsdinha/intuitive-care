from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.modules.operadoras.routes import router as operadoras_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(operadoras_router, prefix="/operadoras", tags=["Operadoras"])

# teste uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)