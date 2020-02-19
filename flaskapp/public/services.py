def get_username(id, uow):
    with uow:
        user = uow.users.get(id=id)
        if user is None:
            return None
        username = user.username
    return username
