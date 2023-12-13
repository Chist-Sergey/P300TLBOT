# python-telegram-bot to work with Telegram api
from telegram import (
    # core
    Update,
    # allows usage of buttons attached to a message
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    # core
    ContextTypes,
)

# get and set a time
from datetime import datetime

# for easier text management
from text_responses import (
    sechude_active,
    search_fail,
    celebrate,
    remove_fail,
    remove_success,
    birthday_set_keyboard_text,
)
# for easier keyboard management
from bot_keyboards import (
    birthday_set_keyboard,
)
# to access database
from database_functions import (
    database_remove,
    database_search_by_date,
    database_search_by_name,
    database_write,
)


async def birthday_loop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Initiates the bot's checking cycle with 'jobQueue'.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # message destination is a chat where it was used
    chat_id = update.effective_message.chat_id
    # tell the bot to run a job repeatedly
    context.job_queue.run_repeating(
        # which job
        callback=birthday_yell,
        # at what interval (in seconds)
        # '42300 seconds' == '12 hours' == 'twice a day'
        interval=42300,
        # when it should start from now (in seconds)
        # '60 seconds' == '1 minute'
        first=60,
        # where the text will be sent
        chat_id=chat_id
    )

    # send a reply message to the user
    await context.bot.send_message(
        chat_id=chat_id,
        text=sechude_active(),
    )


async def birthday_set(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Set a birthday date.

    This function takes up to one optional argument (DATE).

    If the user is already present in a database,
    tell the user their birthday date.

    If there's no such users,
    bring up a message with a keyboard for
    the user to enter their birthday date.

    If the operation was done successfully,
    tell the user that the operation was successful.

    If the operation wasn't done successfully,
    remove this bot's message.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    await update.message.reply_text(
        text=birthday_set_keyboard_text(),
        reply_markup=birthday_set_keyboard()
    )


async def birthday_get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Peek a birthday date.

    This function takes up to one optional argument.

    Using it without any argument will
    send a message with THIS user's birthday date.

    Using it with argument USER will
    send a message with THAT user's birthday date.

    If USER is not in the database,
    tell the user that there's no such USER
    in the database.

    Using it with argument DATE will
    send a message with all users whose birthday
    is matching DATE.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # 'context.args' == 'arguments of the message'
    # 'context.args' may be or may not be present
    if context.args:
        # arguments is a list of strings
        arguments = context.args
        # take the first argument in the message,
        # typically its either a numbers (DATE) or a text (USER)
        first_argument = arguments[0]

        # decide which search function to use
        # 'isnumeric()' == 'consists of mathematical characters'
        if first_argument.isnumeric():
            search_result = database_search_by_date(first_argument)
        else:
            search_result = database_search_by_name(first_argument)
    # if there's no arguments,
    # take a user's name as an argument
    else:
        user_name = update.effective_user.name
        search_result = database_search_by_name(user_name)

    # check for a valid result
    if search_result is None:
        # replace result's 'None' with a fail message
        search_result = search_fail()

    await context.bot.send_message(
        # message destination is a chat where it was used
        chat_id=update.effective_chat.id,
        text=search_result,
    )


async def birthday_yell(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Celebrate a birth day!

    This function takes no arguments.

    Checks for someone's birthday today,
    sends a message if someone has a birthday,
    does nothing if there isn't.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    today = datetime.now()
    # '%d.%m' == 'D.M' == 'Day.Month', ex.: '31.12'
    today_day_and_month = today.strftime('%d.%m')
    birthday_people = database_search_by_date(today_day_and_month)
    if birthday_people:
        await context.bot.send_message(
            # message destination is a chat where it was used
            chat_id=context.job.chat_id,
            text=celebrate(birthday_people),
        )


async def birthday_rm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Remove a birthday.

    This function takes no arguments.

    Take a USER who called this function
    and check if they are in a database.
    If they are, remove their line from
    the database and aknowledge them of this.
    If they aren't, aknowledge them of this.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    message = remove_fail()
    username = update.effective_user.name
    target_line = database_search_by_name(username)
    if target_line:
        message = remove_success()
        database_remove(target_line)

    await context.bot.send_message(
        # message destination is a chat where it was used
        chat_id=update.effective_chat.id,
        text=message,
    )


async def birthday_btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    # JSON really dislikes Dictionaries
    # that's why there's double lists instead
    dates = [
        ['day',   1],
        ['month', 1],
        ['year',  1900],
    ]
    # the intended use of those double-lists is:
    # step 1: get an index
    # step 2: use an index to get the first element
    # step 3: use the same index to get the second element
    # in general, the first list contains the headers to the second list
    # the items in these lists are placed to match eatch other
    # for example,
    # calling 'actions[0][0], actions[0][1]'
    # would result in 'add_two, 2'
    actions = [
        # numbers are present as strings because
        # python is allergic to multi-types lists
        ['add_two', 'substract_one'],
        ['2',       '-1'],
    ]
    states = [
        ['continue', 'abort'],
        ['true!',    'false...'],
    ]

    for date in dates:
        # 'date' is a list with two items
        # first item
        keys = 0
        # second item
        values = 1
        # this text will change troughout the message interaction
        interactive_text = f'{date[keys]}: {date[values]}'

        # waiting for the user to press any button
        await query.answer()
        # 'data' contains a callback value
        # look at keyboards to find what the value might be
        data = query.data

        # check for upper row callback, the math part
        if data in actions[keys]:
            value = actions[keys].index()
            # BAD CODE ALERT!
            # Possible fixes: make values in 'actions' as integers
            date[values] += int(actions[values][value])
        # check for lower row callback, the command part
        if data in states[keys]:
            value = states[keys].index(data)
            interactive_text = states[values][value]
            # once the user have ended their interaction, abort this loop
            break

        await query.edit_message_text(
            text=interactive_text,
            reply_markup=birthday_set_keyboard
        )
