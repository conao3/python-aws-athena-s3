from __future__ import annotations
from typing import Any, Optional

import pydantic
import pydantic.alias_generators


class Argument(pydantic.BaseModel):
    class Config:
        alias_generator = pydantic.alias_generators.to_camel

    type_: str = pydantic.Field(..., alias='@type')
    identity: dict[str, Any]
    catalog_name: str
    query_id: str


def handler(arg_: dict[str, Any]) -> dict[str, Any]:
    arg = Argument.model_validate(arg_)

    return {
        '@type': 'ListSchemasResponse',
        'catalogName':  arg.catalog_name,
        'schemas': [
            's3',
        ]
    }
