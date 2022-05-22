from typing import Optional, Generic, TypeVar
from pydantic.generics import GenericModel
from starlette import status
from starlette.responses import JSONResponse

T = TypeVar('T')


class Result(GenericModel, Generic[T]):
    data: Optional[T] = None
    status: int
    message: Optional[str] = None

    def json(self):
        return JSONResponse(
            status_code=self.status,
            content={
                "status_code": self.status,
                "data": self.data,
                "message": self.message,
            },
        )


class Ok(Result):
    status: int = 200


class Err(Result):
    status: int = 400


def ok(values, message):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status_code": status.HTTP_200_OK,
            "values": values,
            "message": message
        })


def bad_request(values, message):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "status_code": status.HTTP_400_BAD_REQUEST,
            "values": values,
            "message": message
        })
