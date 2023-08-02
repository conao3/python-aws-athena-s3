from __future__ import annotations

from typing import Any

import pydantic
import pydantic.alias_generators


class Argument(pydantic.BaseModel):
    class Config:
        alias_generator = pydantic.alias_generators.to_camel

    type_: str = pydantic.Field(..., alias='@type')
    identity: dict[str, Any]
    query_id: str
    catalog_name: str


def handler(arg_: dict[str, Any]) -> dict[str, Any]:
    arg = Argument.model_validate(arg_)
    return {
        '@type': 'PingResponse',
        'catalogName':  arg.catalog_name,
        'queryId': arg.query_id,
        'sourceType': 'athena_python_sdk',
        # https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-federation-sdk/src/main/java/com/amazonaws/athena/connector/lambda/handlers/FederationCapabilities.java#L33
        'capabilities': 24,
        'serDeVersion': 4,
    }
