import logging
import inspect
import os

def getLogger():
    # Get the name of the caller function (test name or class name)
    loggername = inspect.stack()[1][3]

    # Create logs folder if not present
    log_folder = "logs"
    if not os.path.exists(log_folder):
        os.mkdir(log_folder)

    # Log file path
    log_file = os.path.join(log_folder, "automation.log")

    # Configure logger
    logger = logging.getLogger(loggername)
    if not logger.handlers:  # Avoid duplicate logs
        filehandler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)

    return logger
