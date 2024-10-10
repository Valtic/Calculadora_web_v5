
from flask import Blueprint

blueprint = Blueprint(
    'calc_blueprint',
    __name__,
    url_prefix='/calc'
)
