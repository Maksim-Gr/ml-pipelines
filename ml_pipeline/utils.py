import logging
import time


class Logger:
    """Logger class
    
    
    Usage example:
        logger = Logger("ml-pipeline, debug=True).get()
    """
    
    def __init__(self, name:str, debug:bool = False):
        """Create and set up the logger
        
        Args: 
            name: (str): Name of logger
            debug: (boolean): Log debug messages in console
            
        Returns: 
            logging.Logger: Logger object.
        """
        
        self.logger = logging.getLogger(name)
        
        self.logger.setLevel(logging.INFO)
        
        if debug:
            console_level = logging.DEBUG
        else: 
            console_level = logging.INFO
            
            
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        
        
        console_handler.setFormatter(
            logging.Formatter("%(levelname)s: %(message)s")
        )
        self.logger.addHandler(console_handler)
        
        
        file_handler = logging.FileHandler("/tmp/ml_pipeline.log")
        file_handler.setLevel(logging.DEBUG)
        
        formatter  = logging.Formatter(
            "%(asctime)s:%(name)s:%(levelname)s: %(message)s"
        )
        
        formatter.converter = time.gmtime
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
    def get(self) -> "logging.Logger":
        "Get a prepared logger object"
        return self.logger