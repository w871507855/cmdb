from datetime import datetime
from ninja import Router, Schema
from django.contrib.auth import authenticate
from django.forms import model_to_dict
from server.settings import SECRET_KEY, TOKEN_LIFETIME
from utils.jwt import Jwt

router = Router()

# 用户登录请求的字段
class LoginSchemaIn(Schema):
    username: str
    password: str


@router.post("/login")
def login(request, loginInfo: LoginSchemaIn):
    user_obj = authenticate(username=loginInfo.username, password=loginInfo.password)
    if user_obj:
        role = user_obj.role.all().values("id")
        role_list = []
        for item in role:
            role_list.append(item["id"])
        user_obj_dict = model_to_dict(user_obj)
        user_obj_dict["role"] = role_list
        del user_obj_dict["password"]
        del user_obj_dict["avatar"]
        time_now = int(datetime.now().timestamp())
        jwt = Jwt(SECRET_KEY, user_obj_dict, valid_to=time_now + TOKEN_LIFETIME)
        data = {
            "multi_depart": 1,
            "sysAllDictItems": "q",
            "departs": "e",
            "userInfo": user_obj_dict,
            "token": jwt.encode()
        }
        return {"data": data}
    else:
        return {"msg": "用户或者密码有问题"}