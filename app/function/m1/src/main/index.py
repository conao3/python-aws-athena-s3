from typing import Any
import logging

from aws_lambda_powertools.utilities.typing import LambdaContext

from .. import method


logger = logging.getLogger(__name__)


def handler(event: Any, context: LambdaContext) -> dict[str, Any]:
    logger.info(event)
    res = method.handler(event)
    logger.info(res)
    return res
