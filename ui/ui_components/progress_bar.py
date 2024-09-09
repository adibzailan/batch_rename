from PyQt6.QtWidgets import QWidget, QVBoxLayout, QProgressBar

class ProgressBarWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

    def set_maximum(self, maximum):
        self.progress_bar.setMaximum(maximum)

    def set_value(self, value):
        self.progress_bar.setValue(value)