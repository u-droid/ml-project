import sys

def get_error_message(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = f"Error occured in python script: [{}] Line no. [{}] Error: [{str(error)}]"
    return error_message

class CustomException(Exception)
    def __init__(self, error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = get_error_message(error, error_detail)
        
    def __str__(self):
        return self.error_msg
        