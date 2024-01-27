from utilities.logger import ThreadLogger
import logging.handlers
 
# Create a custom logger for your module
logger = ThreadLogger(__name__)
 
# Implement log rotation (create a new log file when the size reaches 1 MB)
rotating_handler = logging.handlers.RotatingFileHandler('script.log', maxBytes=1e6, backupCount=3)
logger.addHandler(rotating_handler)
 
# Implement log timestamping
formatter = ThreadLogger.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)
 
# Implement log level hierarchy
logger.setLevel(ThreadLogger.DEBUG)
rotating_handler.setLevel(ThreadLogger.DEBUG)
 
# Log aggregation: Optionally, configure log to stream to console as well
console_handler = ThreadLogger.StreamHandler()
logger.addHandler(console_handler)
 
# Log messages
logger.debug("This is a debug message.")
logger.info("Informational message.")
logger.warning("A warning occurred.")
logger.error("An error occurred.")
logger.critical("Critical error!")
