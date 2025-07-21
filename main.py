from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import uvicorn

logger = logging.getLogger(__name__)

try:
    from routers import auth, salary, employee
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
app.include_router(auth.router, prefix="/routers/auth", tags=["auth"])
app.include_router(salary.router, prefix="/routers/salary", tags=["salary"])
app.include_router(employee.router, prefix="/routers/employee", tags=["employee"])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("Starting API server...")
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=1997,
            reload=True,
            log_level="info"
        )
    except Exception as e:
        logger.error(f"Error starting server: {str(e)}")
        raise

if __name__ == "__main__":
    main()