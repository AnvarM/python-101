#logging
import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")



logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex") # create logger with name "ex"

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!") # will catch error and write full traceback to sample.log