from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# =====================================================
# Database
# =====================================================
from app.database.base import Base
from app.database.database import engine

# =====================================================
# Platform Startup
# =====================================================
from app.platform.crud.startup import initialize_crud
from app.platform.events.startup import initialize_events

# =====================================================
# API Routes
# =====================================================
from app.api.login import router as login_router
from app.api.runtime_data import router as runtime_data_router

from app.platform.routes import (
    lookup_router,
    metadata_router,
    runtime_crud_router,
    runtime_router,
    validation_router,
)
from app.platform.workflow.startup import initialize_workflows
from app.platform.workflow.router import router as workflow_router
from app.platform.notifications.router import router as notification_router

from app.routes.company import router as company_router
from app.routes.dashboard import router as dashboard_router
from app.routes.department import router as department_router
from app.routes.plant import router as plant_router
from app.routes.template import router as template_router
from app.routes.uom import router as uom_router



# =====================================================
# Application Lifespan
# =====================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup/shutdown lifecycle.
    """

    # Create database tables
    Base.metadata.create_all(bind=engine)

    yield

    # Future:
    # Close Redis
    # Close Kafka
    # Cleanup resources


# =====================================================
# FastAPI App
# =====================================================
app = FastAPI(
    title="NOVOFLEX ERP",
    description="Enterprise Manufacturing ERP for Plastic Injection Moulding Industry",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# =====================================================
# CORS Configuration
# =====================================================
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://.*-5173\.app\.github\.dev",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Local React Development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# Initialize Platform
# =====================================================
initialize_crud()
initialize_events()
initialize_workflows()

# =====================================================
# Register Routers
# =====================================================
app.include_router(login_router)

app.include_router(dashboard_router)
app.include_router(company_router)
app.include_router(plant_router)
app.include_router(department_router)
app.include_router(uom_router)
app.include_router(template_router)

app.include_router(metadata_router)
app.include_router(runtime_router)
app.include_router(runtime_data_router)
app.include_router(runtime_crud_router)
app.include_router(lookup_router)
app.include_router(validation_router)
app.include_router(workflow_router)
app.include_router(notification_router)

# =====================================================
# Root
# =====================================================
@app.get("/", tags=["System"])
def root():
    return {
        "application": "NOVOFLEX ERP",
        "version": "1.0.0",
        "status": "Running",
    }


# =====================================================
# Health Check
# =====================================================
@app.get("/health", tags=["System"])
def health():
    return {
        "status": "Healthy",
        "database": "Connected",
    }