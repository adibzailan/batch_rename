from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLineEdit, QLabel, QButtonGroup
from PyQt6.QtCore import pyqtSignal

class RenameOptionsWidget(QWidget):
    options_changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.rename_option_group = QButtonGroup()
        self.prefix_suffix_radio = QRadioButton("Add prefix and/or suffix")
        self.swap_radio = QRadioButton("Swap characters")
        self.rename_option_group.addButton(self.prefix_suffix_radio)
        self.rename_option_group.addButton(self.swap_radio)
        self.prefix_suffix_radio.setChecked(True)

        option_layout = QHBoxLayout()
        option_layout.addWidget(QLabel("Rename Option:"))
        option_layout.addWidget(self.prefix_suffix_radio)
        option_layout.addWidget(self.swap_radio)
        layout.addLayout(option_layout)

        self.prefix_suffix_widget = QWidget()
        prefix_suffix_layout = QHBoxLayout(self.prefix_suffix_widget)
        self.prefix_entry = QLineEdit()
        self.suffix_entry = QLineEdit()

        prefix_suffix_layout.addWidget(QLabel("Prefix:"))
        prefix_suffix_layout.addWidget(self.prefix_entry)
        prefix_suffix_layout.addWidget(QLabel("Suffix:"))
        prefix_suffix_layout.addWidget(self.suffix_entry)

        self.swap_widget = QWidget()
        swap_layout = QHBoxLayout(self.swap_widget)
        self.swap_from_entry = QLineEdit()
        self.swap_to_entry = QLineEdit()

        swap_layout.addWidget(QLabel("Swap from:"))
        swap_layout.addWidget(self.swap_from_entry)
        swap_layout.addWidget(QLabel("Swap to:"))
        swap_layout.addWidget(self.swap_to_entry)

        layout.addWidget(self.prefix_suffix_widget)
        layout.addWidget(self.swap_widget)
        self.swap_widget.hide()

        self.prefix_suffix_radio.toggled.connect(self.update_rename_options)
        self.swap_radio.toggled.connect(self.update_rename_options)
        self.prefix_entry.textChanged.connect(self.options_changed.emit)
        self.suffix_entry.textChanged.connect(self.options_changed.emit)
        self.swap_from_entry.textChanged.connect(self.options_changed.emit)
        self.swap_to_entry.textChanged.connect(self.options_changed.emit)

    def update_rename_options(self):
        if self.prefix_suffix_radio.isChecked():
            self.prefix_suffix_widget.show()
            self.swap_widget.hide()
        else:
            self.prefix_suffix_widget.hide()
            self.swap_widget.show()
        self.options_changed.emit()

    def get_rename_operation(self):
        if self.prefix_suffix_radio.isChecked():
            return "prefix_suffix", self.prefix_entry.text(), self.suffix_entry.text()
        else:
            return "swap", self.swap_from_entry.text(), self.swap_to_entry.text()