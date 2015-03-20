from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS

cover = """def cover(f, data):
    return f(set(str(x) for x in data[0]), tuple(set(str(n) for n in coup) for coup in data[1]))
"""

ERR_REPEAT = "Every person should be able to give to a different" \
             " person than he offered the past years"
ERR_COUPLE = "Couples should not give to one another"
ERR_COUNT = "You can find {} chain(s)."
ERR_TYPE = "Wrong result type"
ERR_WRONG_NAMES = "Wrong Family names"


def checker(data, user_result):
    total = data[0]
    family = set(data[1][0])
    couples = tuple(set(x) for x in data[1][1])
    if (not isinstance(user_result, (list, tuple)) or
            any(not isinstance(chain, (list, tuple)) for chain in user_result)):
        return False, ERR_TYPE
    if len(user_result) < total:
        return False, ERR_COUNT.format(total)
    gifted = set()
    for chain in user_result:
        if set(chain) != family or len(chain) != len(family):
            return False, ERR_WRONG_NAMES
        for f, s in zip(chain, chain[1:] + [chain[0]]):
            if {f, s} in couples:
                return False, ERR_COUPLE
            if (f, s) in gifted:
                return False, ERR_REPEAT
            gifted.add((f, s))
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
        function_name="find_chains"
        # add_allowed_modules=[],
        # add_close_builtins=[],
        # remove_allowed_modules=[]
    ).on_ready)
