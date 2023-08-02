from __future__ import annotations
from typing import Any, Optional
import uuid

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
    query_id: str
    catalog_name: str
    table_name: ArgumentTable
    constraints: dict[str, Any]
    schema_: str = pydantic.Field(..., alias='schema')
    partition_columns: list[str]


def handler(arg_: dict[str, Any]) -> dict[str, Any]:
    arg = Argument.model_validate(arg_)

    batch = pyarrow.RecordBatch.from_arrays([], [])
    return {
        '@type': 'GetTableLayoutResponse',
        'catalogName':  arg.catalog_name,
        'tableName': {
            'schemaName': arg.table_name.schema_name,
            'tableName': arg.table_name.table_name,
        },
        'partitions': {
            'aId': str(uuid.uuid4()),
            'schema': subr.pyarrow.encode_object(batch.schema),
            'records': subr.pyarrow.encode_object(batch),
        }
    }
