import random
from telegram.ext import BaseFilter, Filters, MessageHandler
from .utils import db_get_list


class WorkdayEndFilter(BaseFilter):

    def _keyword_detect(self, text):
        persons = db_get_list("person_name")
        locations = db_get_list("location_name")
        person_100 = db_get_list("person_100_name")
        location_100 = db_get_list("location_100_name")
        to_fucks = []
        must_fucks = []
        for i in persons:
            if i in text:
                to_fucks.append(i)
        for i in locations:
            if i in text:
                to_fucks.append(i)
        if to_fucks:
            for i in to_fucks:
                if i in person_100 or i in location_100:
                    must_fucks.append(i)
            if must_fucks:
                to_fuck = random.choice(must_fucks)
            else:
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
    must_fuck_persons = db_get_list("person_100_name")
    must_fuck_locations = db_get_list("location_100_name")
    must_fucks = must_fuck_persons + must_fuck_locations
    if x not in must_fucks:
        for i in range(len(choice_list)):
            choice_list.extend([0, 0, 0])
    times = random.choice(choice_list)
    if times:
        text = ""
        for i in range(times):
            t = random.choice(text_templates)
            text += t.format(x)
            if i < times - 1:
                text += "\r\n"
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

