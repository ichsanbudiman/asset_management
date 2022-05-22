from datetime import datetime
from pydantic.main import BaseModel
from uuid import UUID
from app import app


class FileUploadAsset(BaseModel):
    uuid: UUID
    storage_type: int
    category: int
    path: str
    description: str
    user_uuid: UUID
    created: datetime


class FileUploadRepository:

    def __init__(self):
        self.db_pool = app.state.db_pool

    async def add(self, asset: FileUploadAsset):
        pass

    async def find_by_path(self, asset: FileUploadAsset):
        pass
