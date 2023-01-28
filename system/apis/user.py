from typing import List
from ninja import Router, Schema, Field, ModelSchema, Query
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from system.models import Users, Role
from utils.auth import get_user_info_from_token
from utils.response import Response
from utils.curd import retrieve


router = Router()


class Filters(Schema):
    id: str = Field(None)
    username: str = Field(None)
    mobile: str = Field(None)


class UserSchemaIn(Schema):
    id: str = Field(None)
    username: str
    email: str = Field(None)
    mobile: str = Field(None)
    gender: int = Field(1)
    role: List[int] = Field(None)


class CreateUserSchemaIn(UserSchemaIn):
    password: str


class UpdateUserPasswordIn(Schema):
    id: str = Field(None)
    password: str

class SchemaOut(ModelSchema):
    class Config:
        model = Users
        model_exclude = ["password"]

class Out(Schema):
    message: str
    code: int
    data: SchemaOut


# 根据token获取用户详情
@router.get("/userinfo", response=Out)
def user_info(request):
    user_info = get_user_info_from_token(request=request)
    return Response(code=200, message="查询用户详情成功", data=user_info)


# 查询用户
@router.get("/user", response=List[SchemaOut])
def user(request, filter: Filters = Query(...)):
    query_set = retrieve(request=request, model=Users, filters=filter)
    return query_set


# 创建用户
@router.post("/user", response=SchemaOut)
def create_user(request, data: CreateUserSchemaIn):
    if not isinstance(data, dict):
        data = data.dict()
        del data["id"]
    data["password"] = make_password(data['password'])
    role_ids = data.pop("role")
    roles = Role.objects.filter(id__in=role_ids)
    query_set = Users(**data)
    query_set.save()
    for role in roles:
        query_set.role.add(str(role.id))
    return query_set


# 更新用户基本信息
@router.put("/user/{id}", response=SchemaOut)
def update_user(request, id: int, data: UserSchemaIn):
    dict_data = data.dict()
    insance = get_object_or_404(Users, id=id)
    for attr, value in dict_data.items():
        if attr == "role":
            roles = Role.objects.filter(id__in=value)
            insance.role.set(roles)
        else:
            setattr(insance, attr, value)
    insance.save()
    return insance


# 更新用户密码
@router.put("/user/password/{id}", response=SchemaOut)
def update_password_user(request, id: int, data: UpdateUserPasswordIn):
    dict_data = data.dict()
    insance = get_object_or_404(Users, id=id)
    for attr, value in dict_data.items():
        if attr == "password":
            value = make_password(password=value)
            setattr(insance, attr, value)
    insance.save()
    return insance


# 删除用户
@router.delete("/user/{id}")
def delete_user(request, id: int):
    instance = get_object_or_404(Users, id=id)
    instance.delete()
    return {"message": "删除成功"}
