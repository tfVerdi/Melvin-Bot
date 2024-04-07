import logging
from apis import log_file_path
from logging.config import dictConfig

logging_config = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose":{
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard":{
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers": {
        "console": {
            'level' : "DEBUG",
            'class' : "logging.StreamHandler",
            'formatter': 'standard'
        },
        "console2": {
            'level' : "WARNING",
            'class' : "logging.StreamHandler",
            'formatter': 'standard'
        },
        "file": {
            'level' : "INFO",
            'class' : "logging.FileHandler",
            'filename': log_file_path,
            'mode' : "w",
            'formatter': 'verbose'
        }
    },
    "loggers":{
        "bot": {
            'handlers': ['console'],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            'handlers': ['console2', "file"],
            "level" : "INFO",
            "propagate": False
        }
    }
}

dictConfig(logging_config)