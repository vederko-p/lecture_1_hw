import datetime as _dt
import sqlalchemy as _sql

import database as _database


class Articles(_database.Base):
    __tablename__ = 'Articles'
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    topic = _sql.Column(_sql.String, index=True)
    published = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
