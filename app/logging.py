import logging
import sys

logger = logging.getLogger()
_handler = logging.StreamHandler(stream=sys.stdout)
_formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
_handler.setFormatter(_formatter)
logger.addHandler(_handler)
