import os
from pydantic import BaseModel

class MinioServerConfig(BaseModel):
    url: str
    user: str
    passwd: str


def get_configs():
    minio_server_config = MinioServerConfig(
        url="",
        user="",
        passwd=""
    )
    minio_server_config.url = 'minio:9000'
    minio_server_config.user = os.environ['MINIO_USER']
    minio_server_config.passwd = os.environ['MINIO_PASSWORD']

    return {"minio_server":minio_server_config}



def get_minio_server_configs() -> MinioServerConfig:
    return get_configs()["minio_server"]
