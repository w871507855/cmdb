from ninja import Router
from .apis.login import router as login_router
from .apis.user import router as user_router

system_router = Router()
system_router.add_router("/", login_router, tags=["login"])
system_router.add_router("/", user_router, tags=["user"])