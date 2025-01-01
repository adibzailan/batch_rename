from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class ActionButtonsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create buttons
        self.rename_button = QPushButton("Rename Files")
        self.undo_button = QPushButton("Undo Rename")
        
        # Style buttons
        button_style = """
            QPushButton {
                background: #FF7F7F;
                color: black;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #FF9999;
            }
            QPushButton:disabled {
                background: #FFB3B3;
                color: rgba(0, 0, 0, 0.5);
            }
        """
        self.rename_button.setStyleSheet(button_style)
        self.undo_button.setStyleSheet(button_style)
        
        # Add buttons to layout
        layout.addWidget(self.rename_button)
        layout.addWidget(self.undo_button)
        
        # Initially disable undo button
        self.undo_button.setEnabled(False)
        
    def enable_rename_button(self, enabled):
        self.rename_button.setEnabled(enabled)
        
    def enable_undo_button(self, enabled):
        self.undo_button.setEnabled(enabled)