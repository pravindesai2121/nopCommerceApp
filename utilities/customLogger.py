## This is YouTube Solver code its provide error
# import logging
# import os
# from datetime import datetime

# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log",
#                             format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger

## This is Chatgpt after error its executable solution
import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = ".\\Logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger("automation")
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            file_handler = logging.FileHandler(log_file, mode='a')
            formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s',
                                          datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

