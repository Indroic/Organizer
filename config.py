import configparser
import os

class Config(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        if os.path.exists(os.path.join(os.getcwd(), "config.ini")):
            self.read("config.ini")
        else:
            self.create_config()
        
    
    def create_config(self):
        if not os.path.exists(os.path.join(os.getcwd(), "config.ini")):
            self.add_section("ExtensionsHandler")
            with open(os.path.join(os.getcwd(),"config.ini"), "w") as fp:
                self.write(fp)
            

    
    
    
