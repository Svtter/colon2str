import sys


def type_transfer(type_: str):
    """str => "", int => 1, float => 0.1

    Args:
        type_ (str): _description_
    """
    # (a,b) => 'a': 'b'
    map_dict = {
        "str": '""',
        "int": "1",
        "float": "0.1",
        "dict": "{}",
    }
    return map_dict.get(type_, None)


def colon2equal(colon_str: str, is_space: bool = False):
    if colon_str.find(':') == -1:
        print(f'colon2str: `{colon_str}` is not a legal str.')
        sys.exit(-1)

    res = colon_str.split(":")
    variable_name = res[0].strip(" ")
    variable_type = res[1].strip(" ")

    to_value = type_transfer(variable_type)

    if is_space:
        result = f"{variable_name} = {to_value}"
    else:
        result = f"{variable_name}={to_value}"

    return result


def transfer_multiple(colon2paragraph: str):
    colons = colon2paragraph.split('\n')
    results = [colon2equal(c) for c in colons]
    return "\n".join(results)
