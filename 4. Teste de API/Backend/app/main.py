from fastapi import FastAPI
from app.modules.operadoras.routes import router as operadoras_router

app = FastAPI()

app.include_router(operadoras_router, prefix="/operadoras", tags=["Operadoras"])

# teste uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)