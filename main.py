import sys
import os
from pathlib import Path

from file_handler import FileCollector, Filter
from config import Config

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from ui.dialogs import SuccessDialog, ErrorDialog
from ui.mainWindow import Ui_Main

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setWindowTitle("Organizador")
        
        self.config = Config()
        
        if self.config.getboolean("initial_config", "is_initial") == True:
            self.config.set("initial_config", "is_initial", "False")
            self.config.save_config()
            
            self.create_filters()
            
            self.config = Config()
    
    
        self.dir_dialog = QFileDialog(self)
        self.dir_dialog.setFileMode(QFileDialog.Directory)
        
        self.dir_dialog.setWindowTitle("Seleccionar Carpeta")

        
        self.setStyleSheet(open("styles.css", "r").read())
    
        self.set_list_filters()
    
        self.ui.select_dir.clicked.connect(self.select_dir)
        self.ui.organize_btn.clicked.connect(self.organize)
        
    def set_list_filters(self):
        self.ui.filters_list.addItems(self.config.get_fil())
        
    def select_dir(self):
        self.dir_dialog.exec()
        self.ui.input_dir.setText(self.dir_dialog.selectedFiles()[0])
    
    def create_filters(self):
        images = Filter(
            extensions=["png", "jpg", "jpeg", "gif", "webp"],
            name="Imagenes",
            dir_output=os.path.join(Path.home(), "Images")
        )
        
        images.save()
    
    def organize(self):
        if self.ui.filters_list.selectedItems() and self.dir_dialog.selectedFiles():
            handler = Filter(name = self.ui.filters_list.selectedItems()[0].text())
            handler.load()
            
            files = FileCollector(self.dir_dialog.selectedFiles()[0], handler)
            
            files.move()
            
            self.success = SuccessDialog("Organizado Correctamente!!")
            
            self.success.exec()
        
        else:
            self.error = ErrorDialog("Sleccione una carpeta y un filtro")
            
            self.error.exec()
        
        
    
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())

   
