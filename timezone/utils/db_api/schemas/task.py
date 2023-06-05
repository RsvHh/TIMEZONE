import sqlalchemy
from utils.db_api.async_session import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.Text)
    time = sqlalchemy.Column(sqlalchemy.Text)
