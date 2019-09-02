#logging from multiple modules
import logging
import someotherMod

def main():
    """
    The main entry point of the application
    """
    logging.basicConfig(filename="mySnake.log", level=logging.INFO)
    logging.info("Program started")
    result = otherMod.add(7, 8)
    logging.info("Done!")

if __name__ == "__main__":
    main()
    
    
    
#--------------------------------------------------------------------
# someotherMod.py
import logging

def add(x, y):
    """"""
    logging.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y    