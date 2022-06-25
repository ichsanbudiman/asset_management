
from fastapi import UploadFile
from pydantic import BaseModel


class FileUploadPayloadDTO(BaseModel):
    file: UploadFile
    path: str
    description: str
    tags: str
    bucket: str
