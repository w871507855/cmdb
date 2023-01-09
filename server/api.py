from ninja import NinjaAPI
from asset.router import asset_router

api = NinjaAPI()
api.add_router('/asset/', asset_router)