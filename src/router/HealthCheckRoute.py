from fastapi import APIRouter

router = APIRouter()


class HealthCheckRoute:

    @staticmethod
    @router.get("")
    async def health_check():
        return {"health_check": "Ok"}
