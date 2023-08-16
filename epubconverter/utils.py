import os
import tempfile

def create_temp_directory():
    """
    Create a temporary directory.

    Returns:
    - Path to the temporary directory.
    """
    return tempfile.mkdtemp()

def cleanup_temp_directory(temp_dir):
    """
    Remove a temporary directory and all its contents.

    Args:
    - temp_dir: Path to the temporary directory to remove.
    """
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

def log(message):
    """
    Simple logging function. Can be expanded or replaced with proper logging.

    Args:
    - message: Message to log.
    """
    print("[LOG]", message)

# More utility functions can be added here.
