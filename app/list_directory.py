import logging
import subprocess


def list_directory(directory, params):
    logger = logging.getLogger('tasks')
    result = subprocess.run(['ls', directory, params], capture_output=True)

    if result.returncode != 0:
        error_message = f"Something went wrong when trying to list the directory: ${result.stderr}"
        logger.info(error_message)
        return {"success": False, "message": error_message}
    return {"success": True, "result": str(result.stdout)}