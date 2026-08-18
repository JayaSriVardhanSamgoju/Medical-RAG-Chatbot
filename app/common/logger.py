import logging 
import os 
from datetime import datetime 

LOGS_DIRS="logs"
os.makedirs(LOGS_DIRS,exist_ok=True)

LOG_FILE=os.path.join(LOGS_DIRS,f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

#Logging configuration

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    level=logging.INFO
    )

def get_logger(file_name):
    logger=logging.getLogger(file_name)
    logger.setLevel(logging.INFO)
    return logger
