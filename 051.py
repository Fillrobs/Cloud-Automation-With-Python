# File: main_script.py
from automation_utils import validate_input, log_info, execute_command
 
def deploy_application(name):
    # Validate input
    validate_input(name)
 
    # Log deployment information
    log_info(f"Deploying application: {name}")
 
    # Execute deployment command
    execute_command("deploy")
 
# File: cleanup_script.py
from automation_utils import log_info, execute_command
 
def cleanup_environment():
    # Log cleanup information
    log_info("Cleaning up environment")
 
    # Execute cleanup command
    execute_command("cleanup")
 
