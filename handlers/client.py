from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import client_kb

ALL = ['']


async def text(message: types.Message):
    if (message.text == 'Посмотреть достижения 🤩' and message.from_user.id == 825996300) or message.text == 'waresdgfhjkkndcdjbhadioeklamdjkbhrioailjdkvbfrhifjvnaukrhbfajdvjakbkdajvabjkladjvbjavkksdvbj':
        await bot.send_message(message.from_user.id, '🤩')
        if ALL:
            await bot.send_message(message.from_user.id, "\n\n".join(ALL))
        else:
            await bot.send_message(message.from_user.id, "список пока что пуст)")
    elif message.text == 'Удалить достижения ❌' and message.from_user.id == 825996300:
        await bot.send_message(message.from_user.id, '❌')
        ALL.clear()
        await bot.send_message(message.from_user.id, 'Удалились')
    elif message.text != 'Написать достижение 💌' and message.text != 'Посмотреть достижения 🤩' and message.text != 'Удалить достижения ❌' and message.from_user.id != 825996300 and message.text != 'waresdgfhjkkndcdjbhadioeklamdjkbhrioailjdkvbfrhifjvnaukrhbfajdvjakbkdajvabjkladjvbjavkksdvbj':
        ALL.append(message.text)
        await bot.send_message(message.from_user.id, "Все анонимно сохранено!)")
        await bot.send_message(message.from_user.id, "Продолжай здесь делиться своими достижениями 🤍")


#  @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        if message.from_user.id == 1:
            await bot.send_message(message.from_user.id, '🤖')
            await bot.send_message(message.from_user.id, 'Приветик Карин)',
                                reply_markup=client_kb.AccountMenu)
        else:
            await bot.send_message(message.from_user.id, '💌')
            await bot.send_message(message.from_user.id, 'Привет!) \nСюда ты можешь написать любое свое достижение, которым хочешь анонимно поделиться с другими.')
        #  await message.delete()
    except:
        await message.reply('Общение с ботом через группы - запрещено!')


#  @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'HELP')


#  @dp.message_handler(commands=['admin'])
async def command_admin(message: types.Message):
    await bot.send_message(message.from_user.id, '@KaLiNkA_77')


async def echo(message: types.Message):
    await message.reply("💌")
    ALL.append(message.text)
    print(ALL)
    await message.answer(", ".join(ALL))


def register_handlers_client(dp: Dispatcher):  # Функция регистрации хендлеров
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_admin, commands=['admin'])
    dp.register_message_handler(text)
    dp.register_callback_query_handler(echo, text="A")
