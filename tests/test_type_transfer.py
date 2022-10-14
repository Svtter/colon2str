from colon2equal.transfer import type_transfer


def test_type_transfer():
    cases = (
        ('str', '""'),
        ('int', '1'),
        ('float', '0.1'),
        ('dict', '{}')
    )

    for type_, result in cases:
        assert type_transfer(type_) == result
