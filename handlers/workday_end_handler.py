# coding: utf-8
from datetime import datetime
import logging
import random
import pytz
from telegram.ext import BaseFilter, Filters, MessageHandler
from .utils import db_get_list


log = logging.getLogger()
TZ = pytz.timezone('Asia/Shanghai')
START = 9
END = 18

x = '生番'
global x
y = "person"
global y


class WorkdayEndFilter(BaseFilter):

    def _keyword_detect(self, text):
        persons = db_get_list("person_name")
        locations = db_get_list("location_name")
        to_fucks = []
        for i in persons:
            if i in text:
                to_fucks.append(i)
        for i in locations:
            if i in text:
                to_fucks.append(i)
        if to_fucks:
            to_fuck = random.choice(to_fucks)
            global x
            x = to_fuck
            global y
            if to_fuck in persons:
                y = "person"
            else:
                y = "location"
            return True
        return False

    def filter(self, message):
        text = message.text
        return self._keyword_detect(text)


def deal(bot, update):
    text_templates = db_get_list("%s_temp" % y)
    max_times = 3
    choice_list = list(range(1, max_times+1))
    for i in range(len(choice_list)):
        choice_list.append(0)
    times = random.choice(choice_list)
    if times:
        for i in range(times):
            t = random.choice(text_templates)
            text = t.format(x)
            text_templates.remove(t)
            bot.send_message(
                chat_id=update.message.chat_id,
                text=text,
                reply_to_message_id=update.message.message_id,
            )


dealhigh_handler = MessageHandler(
    Filters.text & WorkdayEndFilter(),
    deal
)
