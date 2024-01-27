from utilities.logger import ThreadLogger
import traceback
 
logger = ThreadLogger(__name__)
 
def process_data(data):
    try:
        # Processing logic that may raise exceptions
        result = data / 0  # Simulating a potential division by zero error
        return result
 
    except Exception as ex:
        # Log the exception along with traceback for postmortem analysis
        logger.error("An error occurred during data processing: %s", ex)
        logger.debug("Traceback: %s", traceback.format_exc())
 
        # Optionally, raise the exception to halt the script or take specific actions
        raise
 
# Example usage
try:
    input_data = 42
    processed_result = process_data(input_data)
    # Continue with the script logic after successful data processing
 
except Exception as script_exception:
    logger.error("Error in script: %s", script_exception)
    # Optionally, perform additional recovery actions or raise the exception
    logger.warning("Script failed during data processing. Implementing additional recovery logic.")
    # ...
 
finally:
    # Optionally, perform cleanup actions or finalize the script execution
    logger.info("Script execution completed.")
 
