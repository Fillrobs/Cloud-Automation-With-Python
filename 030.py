from utilities.logger import ThreadLogger
import requests
from requests.exceptions import RequestException
import time
 
logger = ThreadLogger(__name__)
 
def make_api_call_with_retry(url, data, max_retries=3, retry_delay=5):
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            result = response.json()
            logger.info("API call successful. Result: %s", result)
            return result
 
        except RequestException as req_ex:
            logger.warning("Attempt %d: API call failed. RequestException: %s", attempt, req_ex)
            time.sleep(retry_delay)
 
    logger.error("API call failed after %d attempts.", max_retries)
    # Optionally, raise an exception or take specific actions for failure
    raise
 
# Example usage
api_url = "https://example.com/api/resource"
api_data = {"key": "value"}
 
try:
    result = make_api_call_with_retry(api_url, api_data)
    # Continue with the script logic after a successful API call
 
except Exception as recovery_exception:
    logger.error("Error in script: %s", recovery_exception)
    # Optionally, perform additional recovery actions or raise the exception
    logger.warning("Script failed after retry attempts. Implementing additional recovery logic.")
    # ...
 
finally:
    # Optionally, perform cleanup actions or finalize the script execution
    logger.info("Script execution completed.")
 
