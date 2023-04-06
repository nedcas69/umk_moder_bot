from collections import Counter
from operator import itemgetter

from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, first_name: str, last_name: str, username: str, referral_id: int, status: str,
                   balance: float):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, referral_id=referral_id, status=status,
                    balance=balance)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users

async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()

    return user

async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()


async def count_refs(user_id):
    refs = await User.query.where(User.referral_id == user_id).gino.all()
    return len(refs)

# Функция для проверки аргументов переданных при регистрации
async def check_args(args, user_id: int):
    # Если в аргумент передана пустая строка
    if args == '':
        args = '0'
        return args
    # Если в аргумент переданы не только числа, а и буквы
    elif not args.isnumeric():
        args = '0'
        return args
    # Если в агрумент переданы ТОЛЬКО числа
    elif args.isnumeric():
        # Если аргумент такой-же как и айди пользователя
        if int(args) == user_id:
            args = '0'
            return args
        # Получаем из базы данных пользователя у которого user_id такой-же как и переданный аргумент
        elif await select_user(user_id=int(args)) is None:
            args = '0'
            return args
        # Если наш аргумент прошёл все проверки, то возвращяем его
        else:
            args = str(args)
            return args
    # Если что-то пошло не так
    else:
        args = '0'
        return args

async def change_balance(user_id: int, amount): # Функция изменеия баланса
    user = await select_user(user_id)
    new_balance = user.balance + amount
    try:
        await user.update(balance=new_balance).apply()
        return True
    except Exception:
        return False

async def check_balance(user_id: int, amount): # Функция для проверки баланса
    user = await select_user(user_id=user_id) # Получаем юзера
    try:
        amount = float(amount) # Переводим строку в число
        if user.balance + amount >= 0:
            await change_balance(user_id, amount)
            return True # Если у юзера есть деньги
        elif user.balance + amount < 0: #
            return 'no money' # Если у юзера нету денег
    except Exception: # Если переданы буквы в строке
        return False






async def get_top_referrals():
    users = await User.select('user_id', 'referral_id').where(User.referral_id != 0).gino.all()
    top_referrals = Counter(map(itemgetter('referral_id'), users))
    return sorted(top_referrals.items(), key=lambda item: item[1], reverse=True)







# Функция для получения наибольшего айди в базе данных
# async def get_max_id():
#     max_id = max(await User.select('user_id').gino.all())[0]
#     print(max_id)