from typing import Any

from . import ping_request


mapping = {
    'PingRequest': ping_request.handler,
}


def handler(arg: dict[str, Any]) -> dict[str, Any]:
    type_ = arg.get('@type')
    if type_ is None:
        raise ValueError(f'Missing required argument: @type')

    fn = mapping.get(type_)
    if fn is None:
        raise ValueError(f'Unknown type: {type_}')

    return fn(arg)
