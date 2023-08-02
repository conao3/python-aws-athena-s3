from typing import Any
import logging

from aws_lambda_powertools.utilities.typing import LambdaContext


logger = logging.getLogger(__name__)


def handler(event: Any, context: LambdaContext):
    logger.info(event)
    return {
        "statusCode": 200,
        "body": "Hello, World!"
    }
