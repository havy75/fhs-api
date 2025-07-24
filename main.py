from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import uvicorn
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

try:
    from routers import auth, salary, employee, archivement, quater, yearbonus, onleave,orderlunch

    # from .database.session import create_tables
except ImportError as e:
    logger.error(f"Failed to import required modules: {str(e)}")
    raise

app = FastAPI(title="FHS API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# # Create database tables with error handling
# try:
#     create_tables()
#     logger.info("Database initialized successfully")
# except Exception as e:
#     logger.error(f"Failed to initialize database: {str(e)}")
#     raise

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(salary.router, prefix="/api/salary", tags=["salary"])
app.include_router(employee.router, prefix="/api/employee", tags=["employee"])
app.include_router(archivement.router, prefix="/api/archivement", tags=["archivement"])
app.include_router(quater.router, prefix="/api/quater", tags=["quater"])
app.include_router(yearbonus.router, prefix="/api/yearbonus", tags=["yearbonus"])
app.include_router(onleave.router, prefix="/api/onleave", tags=["onleave"])
app.include_router(orderlunch.router, prefix="/api/orderlunch", tags=["orderlunch"])

@app.get("/", include_in_schema=False)
def root():
    return JSONResponse(content={"status": "ok"})


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("Starting API server...")
        uvicorn.run(
            "main:app", host="0.0.0.0", port=1997, reload=True, log_level="info"
        )
    except Exception as e:
        logger.error(f"Error starting server: {str(e)}")
        raise


if __name__ == "__main__":
    main()
