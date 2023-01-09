from typing import List, Any
from ninja.pagination import PaginationBase
from django.db.models import QuerySet
from ninja import Schema, Field
from ninja.types import DictStrAny




class MyPagination(PaginationBase):
    class Input(Schema):
        pageSize: int = Field(10, gt=0)
        page: int = Field(1, gt=-1)

    class Output(Schema):
        items: List[Any]
        total: int

    def paginate_queryset(self, queryset: QuerySet, pagination: Input, **params: DictStrAny) -> Any:
        offset = pagination.pageSize * (pagination.page - 1)
        limit: int = pagination.pageSize
        return {
            "page": offset,
            "limit": limit,
            "items": queryset[offset: offset + limit],
            "total": self._items_count(queryset)
        }