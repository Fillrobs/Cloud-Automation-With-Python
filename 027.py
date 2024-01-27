from utilities.logger import ThreadLogger
 
# Create a custom logger for your module
logger = ThreadLogger(__name__)
 
# Log messages with different levels
logger.debug("This is a debug message.")
logger.info("Informational message.")
logger.warning("A warning occurred.")
logger.error("An error occurred.")
logger.critical("Critical error!")
 
# Set log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger.setLevel(ThreadLogger.DEBUG)
 
# Format log messages
formatter = ThreadLogger.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setFormatter(formatter)
 
# Direct logs to a file
file_handler = ThreadLogger.FileHandler('script.log')
logger.addHandler(file_handler)
