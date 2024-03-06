from sign_detection.logger import logging
from sign_detection.exception import signException
import sys
# logging.info("welcom to sign detection project")

try:
    a=7/"9"
except Exception as e:
    raise signException(e,sys) from e