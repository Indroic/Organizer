import os
import pathlib
import shutil
from configparser import NoSectionError
from config import Config
from typing import List


class ExtensionHandler:
    def __init__(self, extensions: List[str] = None, name: str = None, dir_output: str = None):
        self.extensions = extensions
        self.name = name
        self.dir_output = dir_output
        self.is_path = False
        
        self.config = Config()
    
        if self.name is not None and self.is_not_none == False:
            self.load()
            
        if not self.validate_path() and self.dir_output != None:
            self.dir_output = self.create_dir()
            
    
    def save(self):
        if self.is_not_none():
            self.validate_path()
            self.config[f"ExtensionsHandler.{self.name}"] = {
                "Name": self.name,
                "Extensions": self.extensions,
                "Directory": self.dir_output,
                "isPath": self.is_path
                }
            with open(os.path.join(os.getcwd(), "config.ini"), "w", encoding="utf-8") as fp:
                self.config.write(fp)
   
            
            
    def load(self) -> bool:
        if self.name is not None:
            try:
                self.name = self.config.get(f"ExtensionsHandler.{self.name}", "Name")
                self.extensions = self.convert_to_list(self.config[f"ExtensionsHandler.{self.name}"]["Extensions"])
                self.dir_output = self.config.get(f"ExtensionsHandler.{self.name}", "Directory")
                self.is_path = self.config.get(f"ExtensionsHandler.{self.name}", "isPath")
                
                return True
            except NoSectionError:
                return False

                
    def convert_to_list(self, string: str) -> List[str]:
        return string.strip("[]").strip('"').replace(" ", "").replace("'", "").split(",")

    def validate_path(self) -> bool:
        try:
            if os.path.isdir(self.dir_output):
                self.is_path = True
                return True
 
            self.is_path = False
            
            return False
    
        except TypeError:
            return False
    
    
    def create_dir(self) -> str:
        if not self.is_path:
            if not os.path.exists(self.dir_output):
                os.makedirs(os.path.join(self.dir_output, self.dir_output.split("/")[-1]), exist_ok=True)
        return os.path.join(self.dir_output, self.dir_output.split("/")[-1])
          
            
    def is_not_none(self) -> bool:
        return all(var is not None for var in [self.extensions, self.dir_output])

class File:
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def move(self, extensionHandler: ExtensionHandler) -> bool:
        if extensionHandler.is_path:
            shutil.move(os.path.join(self.path), extensionHandler.dir_output)
            
        else:    
            shutil.move(os.path.join(self.path), extensionHandler.dir_output)

        return True
    def delete(self):
        os.remove(os.path.join(self.path))
        
    @property
    def details(self) -> dict:
        self.detail = {
            "name": self.name,
            "path": self.path,
            "extension": self.name.split(".")[-1],
            "size": str(round((pathlib.Path(os.path.join(self.path)).stat().st_size / (1024 * 1024)), 2)) + "MB",   
        }
        
        return self.detail

class FileCollector:
    """
    Collects and manages files based on their path and extension.

    Args:
        path (str): The path where the files will be collected from.
        extension (str or list): The file extension(s) to filter the files by.

    Attributes:
        path (str): The path where the files will be collected from.
        extension (str or list): The file extension(s) to filter the files by.
        is_moved (bool): Indicates whether the files have been moved or not.
        files (list): The list of files found.
    """
    
    
    def __init__(self, path: str, extension: ExtensionHandler):
        self.path = path
        self.extension = extension
        self.is_moved = False
        
        
    def filter(self) -> List[File]:
        list_files = []
        
        with os.scandir(self.path) as entries:
            for entry in entries:
                if entry.is_file():
                    for ext in self.extension.extensions:
                        if entry.name.split(".")[-1] == ext:
                            list_files.append(File(entry.path, entry.name))
        
        return list_files
        
        
    def move(self):
        if self.files:
            for file in self.files:
                file.move(self.extension)
            self.is_moved = True

    @property
    def files(self) -> List[File]:
        return self.filter()