from fastapi import APIRouter, UploadFile, File, Form
from controller.FileUploadController import FileUploadController
from dto.FileUploadPayloadDTO import FileUploadPayloadDTO

router = APIRouter()


# https://stackoverflow.com/questions/65408109/how-do-i-receive-image-and-json-data-in-fastapi


class FileRoute:

    @router.post("")
    async def add_new_file(file: UploadFile = File(...),
                           description: str = Form(...),
                           tags: str = Form(...),
                           path: str = Form(...),
                           bucket: str = Form(...)
                           ):
        payload = FileUploadPayloadDTO(
            file=file,
            path=path,
            description=description,
            tags=tags,
            bucket=bucket)
        response = await FileUploadController.add(payload)
        return response
