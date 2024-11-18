import sys
import math
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox


def calculate_flag(upper_edge, lower_edge, junction, layer_thickness):
    try:
        # STEP 1
        step1 = ((upper_edge + lower_edge) / 2) - (junction + 20 / layer_thickness)
        if step1 <= 0:
            return "(Ⅰ/Ⅱ)"

        # STEP 2
        step2 = lower_edge - upper_edge - 40 / layer_thickness
        if step2 <= 0:
            return "(Ⅰ/Ⅱ)"

        # STEP 3
        step3 = ((upper_edge + lower_edge) / 2 * 1 / math.sin(math.radians(63))) - (junction + 20 / layer_thickness)
        if step3 > 0:
            return "(Ⅲ)"
        else:
            return "(Ⅰ/Ⅱ)"
    except Exception as e:
        return f"Error: {e}"


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the window icon
        self.setWindowIcon(QIcon("Logo.ico"))  # 修改此处以使用你的图标

        # Setting up the layout
        layout = QVBoxLayout()
        
        # Input fields
        self.upper_edge_label = QLabel("Superior Border:")
        self.upper_edge_input = QLineEdit()
        
        self.lower_edge_label = QLabel("Inferior Border:")
        self.lower_edge_input = QLineEdit()
        
        self.junction_label = QLabel("EGJ:")
        self.junction_input = QLineEdit()
        
        self.layer_thickness_label = QLabel("Slice Thickness (mm):")
        self.layer_thickness_input = QLineEdit("0.625")  # Default value
        
        # Result display
        self.result_label = QLabel("Siewert Type:")
        self.result_output = QLabel("")
        
        # Buttons
        self.submit_btn = QPushButton("Submit")
        self.clear_btn = QPushButton("Clear")
        
        # Button actions
        self.submit_btn.clicked.connect(self.on_submit)
        self.clear_btn.clicked.connect(self.on_clear)
        
        # Adding widgets to layout
        layout.addWidget(self.upper_edge_label)
        layout.addWidget(self.upper_edge_input)
        
        layout.addWidget(self.lower_edge_label)
        layout.addWidget(self.lower_edge_input)
        
        layout.addWidget(self.junction_label)
        layout.addWidget(self.junction_input)
        
        layout.addWidget(self.layer_thickness_label)
        layout.addWidget(self.layer_thickness_input)
        
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)
        
        # Buttons layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_btn)
        button_layout.addWidget(self.clear_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        self.setWindowTitle("AEG parameters calculator")
        self.resize(600, 400)  # Set the width to twice the original size

    def on_submit(self):
        # Retrieve and validate input
        try:
            upper_edge = float(self.upper_edge_input.text())
            lower_edge = float(self.lower_edge_input.text())
            junction = float(self.junction_input.text())
            layer_thickness = float(self.layer_thickness_input.text())
            
            result = calculate_flag(upper_edge, lower_edge, junction, layer_thickness)
            self.result_output.setText(result)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers.")

    def on_clear(self):
        # Clear all input and output fields
        self.upper_edge_input.clear()
        self.lower_edge_input.clear()
        self.junction_input.clear()
        self.layer_thickness_input.setText("0.625")  # Reset to default value
        self.result_output.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())
