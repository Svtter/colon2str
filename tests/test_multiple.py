from colon2equal.transfer import transfer_multiple


def test_multiple():
    res = transfer_multiple('system:str\nhello:str')
    assert res == 'system=""\nhello=""'
