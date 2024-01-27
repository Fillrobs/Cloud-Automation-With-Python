from utilities.logger import ThreadLogger
import requests
 
# Create a custom logger for your module
logger = ThreadLogger(__name__)
 
def make_api_call(url, data):
    try:
        # Attempt the API call
        response = requests.post(url, json=data)
 
        # Check if the API call was successful (status code 2xx)
        response.raise_for_status()
 
        # Process the API response
        result = response.json()
        logger.info("API call successful. Result: %s", result)
 
    except requests.exceptions.RequestException as req_ex:
        # Handle connection errors, timeouts, and other request exceptions
        logger.error("API call failed. RequestException: %s", req_ex)
        # Optionally, raise the exception to halt the script or take specific actions
        raise
 
    except requests.exceptions.HTTPError as http_ex:
        # Handle HTTP errors (status codes outside the 2xx range)
        logger.error("API call failed. HTTPError: %s", http_ex)
        # Optionally, raise the exception to halt the script or take specific actions
        raise
 
    except Exception as ex:
        # Handle other unexpected exceptions
        logger.error("An unexpected error occurred during the API call: %s", ex)
        # Optionally, raise the exception to halt the script or take specific actions
        raise
 
# Example usage in a CMP Blueprint
try:
    api_url = "https://example.com/api/resource"
    api_data = {"key": "value"}
 
    make_api_call(api_url, api_data)
 
    # Continue with the Blueprint logic after a successful API call
 
except Exception as blueprint_exception:
    # Handle exceptions specific to the Blueprint logic
    logger.error("Error in CMP Blueprint: %s", blueprint_exception)
 
    # Optionally, roll out of the CMP Blueprint or take specific actions
    logger.warning("Rolling out of the CMP Blueprint due to API call failure.")
    # Perform rollback actions or notify administrators
    # ...
 
finally:
    # Optionally, perform cleanup actions or finalize the script execution
    logger.info("Script execution completed.")
 
