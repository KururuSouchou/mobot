# coding: utf-8
from .workday_end_handler import dealhigh_handler
from .start_command_handler import start_command_handler,\
    person_command_handler, fuck_person_command_handler,\
    location_command_handler, fuck_location_command_handler,\
    add_game_command_handler, remove_game_command_handler,\
    price_command_handler, legion_command_handler,\
    person_100_command_handler, location_100_command_handler,\
    person_remove_handler, person_100_remove_handler,\
    location_remove_handler, location_100_remove_handler

HANDLERS = (
    dealhigh_handler,
    start_command_handler,
    person_command_handler,
    fuck_person_command_handler,
    location_command_handler,
    fuck_location_command_handler,
    add_game_command_handler,
    remove_game_command_handler,
    price_command_handler,
    legion_command_handler,
    person_100_command_handler,
    location_100_command_handler,
    person_remove_handler,
    person_100_remove_handler,
    location_remove_handler,
    location_100_remove_handler
)
__all__ = HANDLERS
