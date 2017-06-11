from telegram.ext import CommandHandler
from .utils import db_get_list, db_set_list, db_remove,\
    get_price,set_legion, get_legion


start_text = """
*講粗口*：
    *屌人*
        `/人 人名`
            增加可以屌啲人名，可以多个，半角空格隔开
        `/屌人 模板`
            模板为粗口，必须有一组{}用于插入人名
    *屌地方*
        `/地方 地名`
            参照屌人
        `/屌地方 模板`
            参照屌人

*查steam遊戲價錢*
    *增加关注游戏*
        `/add 游戏id 或 bundle/bundle id`
    *去除关注游戏*
        `/remove 游戏id 或 bundle/bundle id`
    *问价钱*
        `/price`
    *設定地區*
        `/region 地區代號`
            支那：cn, 日本：jp，米國：us，其餘自行查閱
"""


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=start_text,
        parse_mode="Markdown",
    )


def add(bot, update):
    msg_list = update.message.text.split()
    if len(msg_list) == 2:
        game = update.message.text.split()[-1]
        msg = get_price(game)
        if msg != "你讲乜柒":
            db_set_list("user_%s" % str(update.message.from_user.id), [game])
        bot.send_message(
            chat_id=update.message.chat_id,
            text=msg,
            parse_mode="Markdown",
            reply_to_message_id=update.message.message_id,
        )
    else:
        msg = "你想一次加几个呀仆街"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=msg,
            reply_to_message_id=update.message.message_id,
        )


def price(bot, update):
    user_id = "user_%s" % update.message.from_user.id
    games = db_get_list(user_id)
    for i in games:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=i + "\r\n" + get_price(
                i, get_legion(update.message.from_user.id)
                ),
            parse_mode="Markdown",
            reply_to_message_id=update.message.message_id
        )


def remove(bot, update):
    user_id = "user_%s" % update.message.from_user.id
    msg_list = update.message.text.split()
    if len(msg_list) == 2:
        game = update.message.text.split()[-1]
        db_remove(user_id, game)
        bot.send_message(
            chat_id=update.message.chat_id,
            text="搞掂",
            reply_to_message_id=update.message.message_id
        )
    else:
        msg = "你想删乜柒呀仆街"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=msg,
            reply_to_message_id=update.message.message_id
        )


def legion(bot, update):
    msg_list = update.message.text.split()
    if len(msg_list) == 2:
        legion = update.message.text.split()[-1]
        set_legion(update.message.from_user.id, legion)
        bot.send_message(
            chat_id=update.message.chat_id,
            text="搞掂",
            reply_to_message_id=update.message.message_id
        )
    else:
        msg = "你想搞乜柒呀仆街"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=msg,
            reply_to_message_id=update.message.message_id
        )


def p_name(bot, update):
    new_names = update.message.text.split()[1:]
    db_set_list("person_name", new_names)
    bot.send_message(
        chat_id=update.message.chat_id,
        text='可以屌埋{}啦！'.format(str(new_names)),
        reply_to_message_id=update.message.message_id
    )


def p_temp(bot, update):
    if update.message.text.split()[-1].count("{}") == 1:
        new_temp = [update.message.text.split()[-1], ]
        db_set_list("person_temp", new_temp)
        bot.send_message(
            chat_id=update.message.chat_id,
            text='可以用{}屌人啦！'.format(new_temp)
        )
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="粗口模板必须有一组{}， 唔多得唔少得。",
            reply_to_message_id=update.message.message_id
        )


def l_name(bot, update):
    new_names = update.message.text.split()[1:]
    db_set_list("location_name", new_names)
    bot.send_message(
        chat_id=update.message.chat_id,
        text='可以屌埋{}啦！'.format(str(new_names)),
        reply_to_message_id=update.message.message_id
    )


def l_temp(bot, update):
    if update.message.text.count("{}") == 1:
        new_temp = [update.message.text.split()[-1], ]
        db_set_list("location_temp", new_temp)
        bot.send_message(
            chat_id=update.message.chat_id,
            text='可以用{}屌人啦！'.format(new_temp),
            reply_to_message_id=update.message.message_id
        )
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="粗口模板必须有一组{}， 唔多得唔少得。",
            reply_to_message_id=update.message.message_id
        )

        
start_command_handler = CommandHandler('start', start)
person_command_handler = CommandHandler('人', p_name)
fuck_person_command_handler = CommandHandler('屌人', p_temp)
location_command_handler = CommandHandler('地方', l_name)
fuck_location_command_handler = CommandHandler('屌地方', l_temp)
add_game_command_handler = CommandHandler('add', add)
remove_game_command_handler = CommandHandler('remove', remove)
price_command_handler = CommandHandler('price', price)
legion_command_handler = CommandHandler('legion', legion)
