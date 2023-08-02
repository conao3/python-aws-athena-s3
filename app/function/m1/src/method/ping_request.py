from __future__ import annotations
from typing import Any

import pydantic


class Argument(pydantic.BaseModel):
    type_: str = pydantic.Field(..., alias='@type')
    identity: dict[str, Any]
    catalog_name: str = pydantic.Field(..., alias='catalogName')
    query_id: str = pydantic.Field(..., alias='queryId')


def handler(arg_: dict[str, Any]) -> dict[str, Any]:
    arg = Argument.model_validate(arg_)
    return {
        '@type': 'PingResponse',
        'catalogName':  arg.catalog_name,
        'queryId': arg.query_id,
        'sourceType': 'athena_python_sdk',
        # https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-federation-sdk/src/main/java/com/amazonaws/athena/connector/lambda/handlers/FederationCapabilities.java#L33
        'capabilities': 24
    }
