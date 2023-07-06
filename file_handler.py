import os
import pathlib
import shutil
from typing import List, Union

class File:
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def move(self, new_path: str):
        shutil.move(os.path.join(self.path), new_path)

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
    
    
    def __init__(self, path: str, extension: Union[str, list]):
        self.path = path
        self.extension = extension
        self.is_moved = False
        
        
    def filter(self) -> List[File]:
        list_files = []
        
        if isinstance(self.extension, str):
            with os.scandir(self.path) as entries:
                for entry in entries:
                    if entry.name.endswith(self.extension) and entry.is_file():
                        list_files.append(File(entry.path, entry.name))
                        
        if isinstance(self.extension, list):
            with os.scandir(self.path) as entries:
                for entry in entries:
                    if entry.is_file():
                        for ext in self.extension:
                            if entry.name.endswith(ext):
                                list_files.append(File(entry.path, entry.name))
        
        return list_files
        
        
    def move(self, new_path: str):
        if self.files:
            for file in self.files:
                file.move(new_path)
            self.is_moved = True

    @property
    def files(self) -> List[File]:
        return self.filter()