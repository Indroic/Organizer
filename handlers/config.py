import configparser
import os
import appdirs
from typing import List

class Config(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        
        self.configdirectory = appdirs.user_config_dir()
    
        if os.path.exists(os.path.join(self.configdirectory, "organizer_config.ini")):
            self.read(os.path.join(self.configdirectory, "organizer_config.ini"))
        else:
            self.create_config()
    
    def reload(self):
        self.__init__()
    
    def create_config(self):
        if os.path.exists(os.path.join(self.configdirectory, "organizer_config.ini")) == False:
            self.add_section("initial_config")
            self.set("initial_config", "is_initial", str(True))
            with open(os.path.join(self.configdirectory,"organizer_config.ini"), "w") as fp:
                self.write(fp)
    
    def save_config(self):
        with open(os.path.join(self.configdirectory,"organizer_config.ini"), "w", encoding="utf-8") as fp:
            self.write(fp)
                
    def get_filters(self) -> List[str]:
        
        filters =[]
        all_sections = self.sections()
        
        for section in all_sections:
            if section.startswith("Filter"):
                filters.append(self.items(section)[0][1])
                
        return filters
        
            

    
    
    
