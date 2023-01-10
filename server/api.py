from ninja import NinjaAPI
from asset.router import asset_router
from system.router import system_router

api = NinjaAPI()
api.add_router('/asset/', asset_router)
api.add_router('/system/', system_router)
