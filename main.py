import tkinter as tk
from file_handler import FileCollector, ExtensionHandler
from config import Config


extensiones = ExtensionHandler(name="Imagenes")
extensiones.load()

for i in extensiones.extensions:
    print(i)


