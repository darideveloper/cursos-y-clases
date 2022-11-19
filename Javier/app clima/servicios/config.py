import os
import json

current_file = os.path.basename(__file__)
current_folder = os.path.dirname(__file__)  
default_config_path = os.path.join(current_folder, "config.json")

class Config ():
    def __init__ (self, config_path=default_config_path, utf8=False): 
        """Contructor of class

        Args:
            config_path (str/path, optional): Json file for process credentials. Defaults to config.json file.
            utf8 (bool, optional): Read or write data in utf8 format. Defaults to False.
        """
        self.config_path=config_path
        self.utf8=utf8

        config_exist = os.path.isfile(self.config_path)
        if not config_exist: 
            print (f"NOT FILE {self.config_path}")

    def get (self, credential=""): 
        """
        Get specific credential from config file
        """
        
        # Read credentials file 
        if self.utf8: 
            config_file = open(self.config_path, "r", encoding='utf-8')
        else: 
            config_file = open(self.config_path, "r")
        
        # Get specific credential
        try:
            config_data = json.loads(config_file.read())
            return (config_data[credential])
        except Exception as err: 
            # print (err)
            return ""

        # Close file
        config_file.close()