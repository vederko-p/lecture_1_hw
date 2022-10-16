import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


USERNAME = 'myuser'
PASSWORD = 'password'
DATABASE_NAME = 'fastapi_database'
PORT = 5432
DATABASE_URL = f'postgresql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DATABASE_NAME}'

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

Base = _declarative.declarative_base()
