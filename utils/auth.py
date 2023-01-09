from utils.jwt import Jwt
from server.settings import SECRET_KEY


def get_user_info_from_token(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    token = token.split(" ")[1]
    jwt = Jwt(SECRET_KEY)
    value = jwt.decode(SECRET_KEY, token)
    user_info =value.payload
    return user_info