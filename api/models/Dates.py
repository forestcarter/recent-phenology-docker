from api.core import Mixin
from .base import db

# from sqlalchemy.dialects.postgresql import \
#     ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
#     DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
#     INTERVAL, JSON, JSONB, MACADDR, MONEY, VARCHAR, OID, REAL, SMALLINT, TEXT, \
#     TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
#     DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR

from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, DOUBLE_PRECISION, INTEGER


class Dates(Mixin, db.Model):

    __tablename__ = "dates"

    id = db.Column(INTEGER, unique=True, primary_key=True)
    name = db.Column(VARCHAR)
