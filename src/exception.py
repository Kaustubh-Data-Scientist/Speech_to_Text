import sys
from src.logger import logging  # Ensure `src.logger` is implemented correctly

def error_message_detail(error, error_detail: sys) -> str:
    """
    Constructs a detailed error message with file name, line number, and error type.

    Parameters:
    - error: The exception object.
    - error_detail (sys): System-related exception details (traceback).

    Returns:
    - str: A formatted error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"
    
    error_message = (
        f"Error occurred in python script: [{file_name}] "
        f"at line number: [{line_number}] -> {str(error)}"
    )
    return error_message


class CustomException(Exception):
    """
    Custom exception class for detailed error reporting.
    """
    def __init__(self, error_message: str, error_detail: sys):
        """
        Initializes the custom exception with detailed error reporting.

        Parameters:
        - error_message (str): A brief description of the error.
        - error_detail (sys): System-related details about the exception.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        """
        Returns the detailed error message when the exception is printed.
        """
        return self.error_message
