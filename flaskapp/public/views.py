"""Public controllers, including homepage."""
from flask import Blueprint

from . import services, uow

blueprint = Blueprint("public", __name__)


@blueprint.route("/", methods=("GET",))
def home() -> str:
    """The homepage controller.

    Returns
    -------
    str
        TBD
    """
    return "HelloWorld"


@blueprint.route("/users/<user_id>", methods=("GET",))
def get_username(user_id) -> str:
    username = services.get_username(user_id, uow.SqlAlchemyUnitOfWork())
    if username:
        return username
    else:
        return "", 404
