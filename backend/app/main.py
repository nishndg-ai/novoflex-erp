from fastapi import FastAPI
from app.routes.dashboard import router as dashboard_router
from app.api.login import router as login_router
app = FastAPI(
    title="NovoFlex ERP",
    version="1.0",
    description="Enterprise Manufacturing ERP"
)


@app.get("/")
def root():
    return {
        "application": "NovoFlex ERP Enterprise Edition",
        "status": "Running",
        "version": "1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
app.include_router(dashboard_router)
app.include_router(login_router)