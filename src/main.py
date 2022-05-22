from fastapi import FastAPI
from router import HealthCheckRoute;
from router import FileUploadRoute

app = FastAPI()
app.include_router(FileUploadRoute.router, prefix="/file-upload", tags=['file-upload'])
app.include_router(HealthCheckRoute.router, prefix="/health", tags=['health'])
