import logging

from .codes import *
from .commands import *  # NOTE: Must be imported to find inheritors
from .events import *  # NOTE: Must be imported to find inheritors

"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler() # sends output to stderr
console_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logger.addHandler(console_handler)
"""