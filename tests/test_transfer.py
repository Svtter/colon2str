from time import clock_getres
from colon2equal.transfer import colon2equal


def test_colon2equal():
    cases = (
        ("system: str", False, 'system=""'),
        ("system: str", True, 'system = ""'),
        ("size: int", False, "size=1"),
    )
    for colon_str, is_space, result in cases:
        assert colon2equal(colon_str, is_space) == result
