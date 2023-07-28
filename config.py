import configparser
import os
import pathlib
from typing import List

class Config(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        if os.path.exists(os.path.join(os.getcwd(), "config.ini")):
            self.read("config.ini")
        else:
            self.create_config()
        
    
    def create_config(self):
        if not os.path.exists(os.path.join(os.getcwd(), "config.ini")):
            self.add_section("initial_config")
            self.set("initial_config", "is_initial", str(True))
            with open(os.path.join(os.getcwd(),"config.ini"), "w") as fp:
                self.write(fp)
    
    def save_config(self):
        with open(os.path.join(pathlib.Path(__file__).parent, "config.ini"), "w", encoding="utf-8") as fp:
            self.write(fp)
                
    def get_filters(self) -> List[str]:
        
        handlers =[]
        all_sections = self.sections()
        
        for section in all_sections:
            if section.startswith("Filter"):
                handlers.append(self.items(section)[0][1])
                
        return handlers
        
            

    
    
    
