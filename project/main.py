"""FastAPI main class."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project.config import get_settings
from project.exceptions.exception_handler import register_exceptions_handler
from project.routers import actuator, candidates, users, votes

# Import settings

settings = get_settings()

# Create the app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.DOMAIN_FRONTEND],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register igs_classes handler
register_exceptions_handler(app)

# Add routers
app.include_router(actuator.router)
app.include_router(candidates.router)
app.include_router(users.router)
app.include_router(votes.router)
