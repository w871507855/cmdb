from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Schema
from ninja.pagination import paginate
from .models import Asset
from utils.ninga import MyPagination


router = Router()


# 输入
class AssetShemaIn(ModelSchema):
    class Config:
        model = Asset
        model_fields = "__all__"


# 输出
class AssetShemaOut(ModelSchema):
    class Config:
        model = Asset
        model_fields = "__all__"


# class Out(Schema):
#     code: str = 200
#     msg: str
#     data: AssetShemaOut or List[AssetShemaOut]


# 查询所有资产
@router.get("/asset", response=List[AssetShemaOut])
@paginate(MyPagination)
def list_asset(request):
    query_set = Asset.objects.all()
    return query_set


# 根据id查询资产
@router.get("/asset/{id}", response=AssetShemaOut)
def get_asset(request, id: int):
    query = get_object_or_404(Asset, id=id)
    return query


# 更新资产
@router.put("/asset/{id}", response=AssetShemaOut)
def update_asset(request, id: int, data: AssetShemaIn):
    dict_data = data.dict()
    instance = get_object_or_404(Asset, id=id)
    for attr, value in dict_data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance

# 创建资产
@router.post("/asset", response=AssetShemaOut)
def create_asset(request, data: AssetShemaIn):
    if not isinstance(data, dict):
        data = data.dict()
    query = Asset.objects.create(**data)
    return query

# 删除资产
@router.delete("/asset/{id}")
def delete_asset(request, id: int):
    instance = get_object_or_404(Asset, id=id)
    instance.delete()
    return {"success": True}




