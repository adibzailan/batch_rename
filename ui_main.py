import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import BatchRenameUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BatchRenameUI()
    window.show()
    sys.exit(app.exec())