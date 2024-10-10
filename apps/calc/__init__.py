
from flask import Blueprint

blueprint = Blueprint(
    'calc_blueroutes',
    __name__,
    url_prefix='/calc'
)
