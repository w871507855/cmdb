from ninja import Router
from .api import router

asset_router = Router()
asset_router.add_router("/", router, tags=["asset"])