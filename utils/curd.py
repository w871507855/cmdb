
def retrieve(request, model, filters):
    if filters is not None:
        for attr, value in filters.__dict__.items():
            if getattr(filters, attr) == "":
                setattr(filters, attr, None)
        query_set = model.objects.filter(**filters.dict(exclude_none=True))
    else:
        query_set = model.objects.all()
    return query_set