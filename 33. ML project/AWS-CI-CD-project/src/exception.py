import sys
from src.logger import logging


def get_detailed_error_message(error, error_detail: sys) -> str:
    """
    Returns a detailed error message with filename and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in script: [{file_name}] at line [{line_number}] with message: {str(error)}"


class CustomException(Exception):
    """
    Custom exception class for structured error handling and logging.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the custom exception with detailed traceback info.
        """
        super().__init__(error_message)
        self.error_message = get_detailed_error_message(error_message, error_detail)

        # Log the error when it's initialized
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
