from flask import Blueprint, request, json
from api.models import db, Film, Dates
from api import models
from api.core import create_response, serialize_list, logger
from sqlalchemy import inspect
import geoalchemy2.functions as geofunc

######

main = Blueprint("main", __name__)  # initialize blueprint


@main.route("/films", methods=["GET"])
def get_films():
    films = Film.query.all()
    return create_response(data={"films": serialize_list(films)})


@main.route("/getdates", methods=["GET"])
def getdates():
    films = Dates.query.all()
    return create_response(data={"dates": serialize_list(films)})
