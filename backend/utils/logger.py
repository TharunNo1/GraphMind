import logging
from config import Config

# Configure logging
def create_logger():
    logger = logging.getLogger('GraphAI')
    handler = logging.StreamHandler()  
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(Config.LOG_LEVEL)
    return logger

logger = create_logger()
