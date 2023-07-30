
import sys
import os


from handlers.file_handler import FileCollector, Filter
from handlers.config import Config

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from ui.dialogs import SuccessDialog, ErrorDialog
from ui.edit_filter_form_ui import Ui_EditFilter
from ui.mainWindow_ui import Ui_Main
from handlers.extensions import *

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setWindowTitle("Organizer")
        
        self.config = Config()
        
        if self.config.getboolean("initial_config", "is_initial") == True:
            self.config.set("initial_config", "is_initial", "False")
            self.config.save_config()
            
            self.create_inital_filters()
            
            self.config.reload()
    
    
        self.dir_organize_dialog = QFileDialog(self)
        self.dir_organize_dialog.setFileMode(QFileDialog.Directory)
        
        self.dir_organize_dialog.setWindowTitle("Select Directory")
        
        
        self.dir_output_dialog = QFileDialog(self)

        self.dir_output_dialog.setFileMode(QFileDialog.Directory)

        self.dir_output_dialog.setWindowTitle("Select Directory")

        self.error = ErrorDialog()
        self.success = SuccessDialog()

        
        self.setStyleSheet(open("ui/source/styles/styles.css", "r").read())
    
        self.set_list_filters()
    
        self.ui.select_dir.clicked.connect(self.select_dir_organize)
        self.ui.dir_select_btn.clicked.connect(self.select_dir_output)
        self.ui.organize_btn.clicked.connect(self.organize)
        self.ui.add_extension_btn.clicked.connect(self.add_extension_list)
        self.ui.create_filter.clicked.connect(self.create_filter)
        self.ui.delete_btn.clicked.connect(self.delete_filter)
        self.ui.edit_btn.clicked.connect(self.edit_filter)
        
        self.ui.gear_btn.clicked.connect(self.view_config)
        self.ui.back_btn.clicked.connect(self.home)
        
    def set_list_filters(self):
        self.config.reload()
        
        self.ui.filters_list.clear()
        self.ui.filters_created_list.clear()
        if self.config.get_filters() != []:
            self.ui.filters_list.addItems(self.config.get_filters())
            self.ui.filters_created_list.addItems(self.config.get_filters())
        else:
            self.error.set_message("No filters found")
            self.error.exec()
        
    def select_dir_organize(self):
        self.dir_organize_dialog.exec()
        self.ui.input_dir.setText(self.dir_organize_dialog.selectedFiles()[0])

    def select_dir_output(self):
        self.dir_output_dialog.exec()
        self.ui.dir_input.setText(self.dir_output_dialog.selectedFiles()[0])
    
    def create_inital_filters(self):
        Filter(extensions= IMAGES,name="Images", dir_output=os.path.join("Images")).save()
        Filter(extensions= VIDEO,name="Videos", dir_output=os.path.join("Videos")).save()
        Filter(extensions= AUDIO,name="Audio", dir_output=os.path.join("Audios")).save()
        Filter(extensions= DOCUMENTS,name="Documents", dir_output=os.path.join("Documents")).save()
        Filter(extensions= EXECUTABLES,name="Executables", dir_output=os.path.join("Executables")).save()
        Filter(extensions= COMPRESSED,name="Compressed", dir_output=os.path.join("Compressed")).save()    
       
    def organize(self):
        
        if not  self.dir_organize_dialog.selectedFiles():
            self.error.set_message("Select a directory")
            self.error.exec()
            
            return None
        
        if not self.ui.filters_list.selectedItems():
            self.error.set_message("Select a filter")
            self.error.exec()
            
            return None

        
        handler = Filter(name = self.ui.filters_list.selectedItems()[0].text())
        handler.load()
        
        files = FileCollector(self.dir_organize_dialog.selectedFiles()[0], handler)
        
        files.move()
        
        self.success.set_message("Organizado Correctamemte!!")
        
        self.success.exec()

        return None
        
    def view_config(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def home(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def add_extension_list(self):
        lista = [self.ui.extensions_list.item(row).text() for row in range(self.ui.extensions_list.count())]
        if not self.ui.add_extension_input.text():
            return
        
        if self.ui.add_extension_input.text() in lista:
            self.ui.add_extension_input.clear()
            return
        
        lista.append(self.ui.add_extension_input.text())
        self.ui.add_extension_input.clear()
        self.ui.extensions_list.clear()
        self.ui.extensions_list.addItems(lista)
        
    def create_filter(self):
        if not self.ui.name_input.text():
            self.error.set_message("Write filter name")
            self.error.exec()
            return None
        
        if Filter(name=self.ui.name_input.text()).load():
            self.error.set_message("Filter already exists")
            self.error.exec()
            return None
        
        if not self.ui.dir_input.text():
            self.error.set_message("Select a directory")
            self.error.exec()
            return None
        if not self.ui.extensions_list.count():
            self.error.set_message("No Extensions added")
            self.error.exec()
            return None
        
        items = [self.ui.extensions_list.item(row).text() for row in range(self.ui.extensions_list.count())]
        new_filter = Filter(
            name=self.ui.name_input.text(),
            extensions=items,
            dir_output=self.ui.dir_input.text()
            )
        
        new_filter.save()
        
        self.success.set_message("Created Filter")
        self.success.exec()
        
        self.ui.extensions_list.clear()
        self.ui.name_input.clear()
        self.ui.dir_input.clear() 
        
        self.set_list_filters()
        
        return None
    
    def delete_filter(self):
        if self.ui.filters_created_list.selectedItems():
            filter = Filter(name=self.ui.filters_created_list.selectedItems()[0].text())
            filter.load()   
            
            filter.delete()
            
            
            self.set_list_filters() 

    def edit_filter(self):
        if self.ui.filters_created_list.selectedItems():
            filter = Filter(name=self.ui.filters_created_list.selectedItems()[0].text())
            filter.load()
            edit = Ui_EditFilter(filter)
            edit.exec()
            self.set_list_filters()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())

   
