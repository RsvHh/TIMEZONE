from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import validators


async def create_markup(tip, row_width, *args):
    """
    Створює готовий markup з кнопками\n
    Якщо потрібно inline: tip="inline", якщо reply: tip="reply"\n
    row_width вказує на кількість стовбців\n
    *args - списки, в яких\n
    [0]="назва кнопок",\n
    [1] (тільки для inline)="data for callback" або [1] (тільки для inline)="url"\n
    :param tip: "inline" or "reply"
    :param row_width: int
    :param args: list, list, list, ...
    :return: aiogram.types.Markup
    """
    if tip == 'inline':
        markup = InlineKeyboardMarkup(row_width=row_width)
        markup.add(*await create_btns(tip, *args))
    else:
        markup = ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=True)
        markup.add(*await create_btns(tip, *args))
    return markup


async def create_btns(tip, *args):
    """
    Створює готові кнопки для markup\n
    Якщо потрібні inline, то tip="inline", якщо reply - tip="reply"\n
    *args - списки, в яких [0]="назва кнопки", [1] (тільки для inline)="data for callback"\n
    :param tip: "inline" or "reply"
    :param args: list, list, list, ...
    :return: [aiogram.types.Buttons, aiogram.types.Buttons, ...]
    """
    result = []
    for params in args:
        if tip == 'inline':
            if validators.url(params[1]):
                result.append(InlineKeyboardButton(params[0], url=params[1]))
            else:
                result.append(InlineKeyboardButton(params[0], callback_data=params[1]))
        else:
            result.append(KeyboardButton(params[0]))
    return result
