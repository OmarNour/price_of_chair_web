# views are the end point of the API that's related to the user
from flask import Blueprint

item_blueprint = Blueprint('items', __name__)

@item_blueprint.route('/item/<string:name>')
def item_page(name):
    pass


