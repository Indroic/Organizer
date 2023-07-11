import tkinter as tk
from file_handler import FileCollector, ExtensionHandler
from config import Config


extensions = ExtensionHandler(extensions=["mp4", "avi"], name="Video", dir_output="C:\\Users\\David Latosefki\\Videos\\probando")
extensions.save()
files = FileCollector("C:\\Users\\David Latosefki\\Downloads", extensions)
files.move()