import json
from typing import Any
from django.http import HttpResponse
from utils.jwt import DateEncoder


class Response(HttpResponse):
    def __init__(self, data=None, message="success", code=200, *args: Any, **kwargs: Any) -> None:
        std_data = {
            "code": code,
            "data": data,
            "message": message
        }
        data = json.dumps(std_data, cls=DateEncoder)
        super().__init__(data, *args, **kwargs)