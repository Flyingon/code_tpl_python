from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


# whoami health check
async def health_check():
    return ""


# new crack captcha endpoint
async def crack_captcha(body):
    return ""


router.add_api_route(path="/whoami", endpoint=health_check, methods=["GET"])
router.add_api_route("/v1/test", endpoint=crack_captcha, methods=["POST"])

app.include_router(router)
