from io import BufferedIOBase

from pydantic import BaseModel
from minio.api import Minio
from dto.FileUploadPayloadDTO import FileUploadPayloadDTO
from util.Response import Err, Ok, Result
from util.Devops import get_minio_server_configs


class AddFileResponseDTO(BaseModel):
    object_fullname: str


class RemoveFileResponseDTO(BaseModel):
    object_fullname: str


class FileUploadController:
    @staticmethod
    async def add(payload: FileUploadPayloadDTO) -> Result[AddFileResponseDTO]:
        configs = get_minio_server_configs()
        client = Minio(
            configs.url,
            configs.user,
            configs.passwd,
            secure=False)

        found = client.bucket_exists(payload.bucket)

        if not found:
            return Err(status=404)

        bytes_io: BufferedIOBase = payload.file.file._file
        # bytes_io_length = bytes_io.getbuffer().nbytes
        object_fullname = payload.path + '/' + payload.file.filename

        client.put_object(
                bucket_name=payload.bucket,
                object_name=object_fullname,
                data=bytes_io,
                length=-1,
                part_size=10*1024*1024)

        return Ok(data=AddFileResponseDTO(object_fullname=object_fullname))

    @staticmethod
    async def remove(object_fullname: str) -> Result[RemoveFileResponseDTO]:
        configs = get_minio_server_configs()
        client = Minio(
            configs.url,
            configs.user,
            configs.passwd,
            secure=False)

        found = client.bucket_exists(payload.bucket)

        if not found:
            return Err(status=404)

        return Ok(data=AddFileResponseDTO(object_fullname=object_fullname))
