import tkinter as tk
from file_handler import FileCollector, ExtensionHandler
from config import Config


extensions = ExtensionHandler(name="Imagenes")
if extensions.load():
    files = FileCollector("C:\\Users\\David Latosefki\\Downloads", extensions)

    for file in files.files:
        print(file.details["name"])