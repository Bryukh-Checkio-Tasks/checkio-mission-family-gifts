from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS

cover = """def cover(f, data):
    return f(tuple(tuple(d) for d in data))"""


def checker(data, user_result):
    return True, "Ok"


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,
            'python-3': cover
        },
        checker=checker,
        function_name="find_cycle"
        # add_allowed_modules=[],
        # add_close_builtins=[],
        # remove_allowed_modules=[]
    ).on_ready)
