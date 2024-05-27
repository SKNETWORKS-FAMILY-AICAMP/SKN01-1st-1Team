# db logger
from log.logg import Logger
from log.loggdb_mysql import DatabaseHandler 
import logging

if __name__ == "__main__":
    logger = logging.getLogger('testdb')     
    logger.setLevel(logging.DEBUG)              
    mysqlHandler = DatabaseHandler()           
    logger.addHandler(mysqlHandler)            

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    logger.debug("디버깅")         
    logger.info("잘됨")         
    logger.warning("경고")         
    logger.critical("심각")         