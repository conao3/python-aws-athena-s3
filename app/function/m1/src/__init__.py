import json
import logging.config
import os
from datetime import datetime

logger = logging.getLogger(__name__)


class JsonFormatter(logging.Formatter):
    def formatMessage(self, record: logging.LogRecord) -> str:
        default_dict = {
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
            'location': f'{record.pathname}:{record.lineno}',
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
        }
        extra_dict = {
            key: val
            for key, val
            in record.__dict__.items()
            if key.startswith('$')
        }
        return json.dumps(default_dict | extra_dict, ensure_ascii=False, default=str)


class Formatter(logging.Formatter):
    def formatMessage(self, record: logging.LogRecord) -> str:
        if os.environ.get('LAMBDA_TASK_ROOT'):
            return super().formatMessage(record).replace('\n', '\r')

        return super().formatMessage(record)


if os.environ.get('LAMBDA_TASK_ROOT'):
    import logging.config
    import pathlib

    import yaml

    # Disable all AWS managed handlers
    logging.getLogger().handlers.clear()

    with open(pathlib.Path() / 'src' / 'logging.conf.yml', 'r') as f:
        logging.config.dictConfig(yaml.safe_load(f))
