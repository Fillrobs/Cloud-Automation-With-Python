from common.methods import set_progress
from utilities.logger import ThreadLogger
 
logger = ThreadLogger(__name__)
 
def run(job, *args, **kwargs):
 
    try:
        # Perform some actions or tasks here
        logger.info("LOGGER:Starting the blueprint execution...")
        set_progress("Executing the first step...")
        # ... (perform actions)
 
        logger.debug("LOGGER:This is a debug message.")
        set_progress("Executing the second step...")
        # ... (perform more actions)
        
        # result = 10 / 0  # This will raise a ZeroDivisionError
        logger.warning("LOGGER:This is a warning message.")
        set_progress("Blueprint execution completed.")
        return "SUCCESS", "This Code ran without errors", ""
    except Exception as e:
        logger.error(f"LOGGER:Error occurred: {e}")
        set_progress(f"Error occurred: {e}")
        # Handle the error or exception accordingly
        return "FAILURE", "This Code ran with errors", f"{e}"
 
