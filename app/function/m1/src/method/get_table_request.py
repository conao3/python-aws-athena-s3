from __future__ import annotations
from typing import Any, Optional

import pydantic
import pydantic.alias_generators
import pyarrow

from .. import subr


class ArgumentTable(pydantic.BaseModel):
    class Config:
        alias_generator = pydantic.alias_generators.to_camel

    schema_name: str
    table_name: str


class Argument(pydantic.BaseModel):
    class Config:
        alias_generator = pydantic.alias_generators.to_camel

    type_: str = pydantic.Field(..., alias='@type')
    identity: dict[str, Any]
    catalog_name: str
    query_id: str
    table_name: ArgumentTable


def handler(arg_: dict[str, Any]) -> dict[str, Any]:
    arg = Argument.model_validate(arg_)

    return {
        '@type': 'GetTableResponse',
        'catalogName':  arg.catalog_name,
        'tableName': {
            'schemaName': arg.table_name.schema_name,
            'tableName': arg.table_name.table_name,
        },
        'schema': subr.pyarrow.encode_object(pyarrow.schema([
            ('id', pyarrow.string()),
            ('name', pyarrow.string()),
        ])),
        'partitionColumns': [],
    }
