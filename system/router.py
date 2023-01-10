from ninja import Router
from .apis.login import router as login_router

system_router = Router()
system_router.add_router("/", login_router, tags=["login"])