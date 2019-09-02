#logging_datailed

import logging
import newModule

def main():
    """
    The main entry point of the application
    """
    logger = logging.getLogger("exampleApp") # creating logger instance "exampleApp"
    logger.setLevel(logging.INFO) # set logging level from INFO

    # create the logging file handler
    fh = logging.FileHandler("new_snake.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = newModule.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()
    
    
#--------------------------------------------------------------------
# newModule.py
import logging
module_logger = logging.getLogger("exampleApp.newModule")

def add(x, y):
    """"""
    logger = logging.getLogger("exampleApp.newModule.add")
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y    