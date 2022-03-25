from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta, engine

posters = Table(
    "posters",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_media", Integer),
    Column("morning_poster", Text),
    Column("daily_poster", Text),
    Column("evening_poster", Text)
)

meta.create_all(engine)