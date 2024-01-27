from utilities.logger import ThreadLogger
import requests
from requests.exceptions import RequestException
 
logger = ThreadLogger(__name__)
 
def make_fallback_api_call(primary_url, fallback_url, data):
    try:
        # Attempt the API call on the primary endpoint
        response = requests.post(primary_url, json=data)
        response.raise_for_status()
        result = response.json()
        logger.info("Primary API call successful. Result: %s", result)
        return result
 
    except RequestException as primary_req_ex:
        logger.warning("Primary API call failed. Attempting fallback: %s", primary_req_ex)
 
        try:
            # Attempt the API call on the fallback endpoint
            response = requests.post(fallback_url, json=data)
            response.raise_for_status()
            result = response.json()
            logger.info("Fallback API call successful. Result: %s", result)
            return result
 
        except RequestException as fallback_req_ex:
            logger.error("Fallback API call failed. Both primary and fallback endpoints are unreachable.")
            # Optionally, raise an exception or take specific actions for failure
            raise
 
# Example usage
primary_api_url = "https://primary.example.com/api/resource"
fallback_api_url = "https://fallback.example.com/api/resource"
api_data = {"key": "value"}
 
try:
    result = make_fallback_api_call(primary_api_url, fallback_api_url, api_data)
    # Continue with the script logic after a successful API call
 
except Exception as recovery_exception:
    logger.error("Error in script: %s", recovery_exception)
    # Optionally, perform additional recovery actions or raise the exception
    logger.warning("Script failed after attempting both primary and fallback API calls.")
    # ...
 
finally:
    # Optionally, perform cleanup actions or finalize the script execution
    logger.info("Script execution completed.")
 
