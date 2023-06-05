import pendulum
from utils.db_api import async_session
from utils.db_api.schemas.task import Task
from sqlalchemy import delete


async def create_session():
    async_session.global_init('db/task.db')
    db_sess = async_session.create_session()
    return db_sess


# async def check_task(u3l: str):
#     """
#     Проверяет link в бд\n
#     :param u3l: link
#     :return: True или False
#     """
#     db_sess = await create_session()
#     for task in db_sess.query(Task).filter(Task.url == u3l):
#         db_sess.close()
#         return True
#     db_sess.close()
#     return False


async def add_task(user_id: int, time: str, name: str):
    """
    Добавляет задачу в db\n
    :param user_id: id пользователя\n
    :param time: время в формате: "16:23"\n
    :param name: описание задачи\n
    """
    task = Task()
    task.user_id = user_id
    task.time = time
    task.name = name

    db_sess = await create_session()
    db_sess.add(task)
    db_sess.commit()
    db_sess.close()


async def check_time(id_: int):
    data = await return_data(id_)
    if data.time == ':'.join([str(pendulum.now('Europe/Kiev').hour), str(pendulum.now('Europe/Kiev').minute)]):
        return True
    return False


async def return_all():
    """
    Возвращает все задачи
    """
    db_sess = await create_session()
    l1st = db_sess.query(Task).all()
    db_sess.close()
    return l1st


async def delete_all(id_: int):
    """
    Удаляет задачи из бд\n
    :param id_: id пользователя
    """
    db_sess = await create_session()

    sq = delete(Task).where(Task.user_id == id_)
    db_sess.execute(sq)

    db_sess.commit()
    db_sess.close()


async def deanon(id_: int) -> Task:
    """
    Возвращает задачу в виде Task\n
    :param id_: id пользователя
    """
    db_sess = await create_session()
    data = db_sess.query(Task).filter(Task.user_id == id_).all()
    db_sess.close()
    return data


async def return_data(id_: int) -> Task:
    """
    Возвращает задачу в виде Task\n
    :param id_: id задачи
    """
    db_sess = await create_session()
    data = db_sess.query(Task).filter(Task.id == id_).first()
    db_sess.close()
    return data
