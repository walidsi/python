import logging

FILE_LOGGING = True

FORMATTER_STRING = '%(asctime)s:%(filename)s:%(levelname)s:%(message)s'

# Default call witll create a stream logger
logging.basicConfig(level=logging.DEBUG, format='%(message)s') 

if FILE_LOGGING: # add file logger as well
    root = logging.getLogger()
    file_handler = logging.FileHandler('main.log')
    file_handler.setFormatter(logging.Formatter(FORMATTER_STRING))
    file_handler.setLevel(logging.DEBUG)
    root.addHandler(file_handler)


import employee
import math_funcs


def main():
    logging.info(__name__)


if __name__ == "__main__":
    main()
