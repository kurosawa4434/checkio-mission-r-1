def checker(answer): return sorted(answer)

from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io_template import CheckiOReferee
from checkio.referees import cover_codes

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cheker = checker,
        function_name={
            "python": "riichi_mahjong_sets"
        },
        cover_code={
            'python-3': {}
            }
    ).on_ready)
