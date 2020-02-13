"""Public controllers, including homepage."""
from flask import Blueprint

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
