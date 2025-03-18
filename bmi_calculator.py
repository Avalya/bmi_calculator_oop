import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QWidget, QMenuBar,
                             QAction, QMessageBox)
from PyQt5.QtCore import Qt

class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 400, 250)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.weight_label = QLabel("Weight (kg):")
        self.weight_input = QLineEdit()
        self.layout.addWidget(self.weight_label)
        self.layout.addWidget(self.weight_input)

        self.height_label = QLabel("Height (m):")
        self.height_input = QLineEdit()
        self.layout.addWidget(self.height_label)
        self.layout.addWidget(self.height_input)

        self.calculate_button = QPushButton("Calculate BMI")
        self.calculate_button.clicked.connect(self.calculate_bmi)
        self.layout.addWidget(self.calculate_button)

        self.bmi_result_label = QLabel("BMI: ")
        self.layout.addWidget(self.bmi_result_label)

        self.status_label = QLabel("Status: ")
        self.layout.addWidget(self.status_label)

        self.central_widget.setLayout(self.layout)

        self._create_menu()

    def _create_menu(self):
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self._clear_fields)
        file_menu.addAction(clear_action)

        # Help Menu
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("How to Use", self)
        about_action.triggered.connect(self._show_usage_info)
        help_menu.addAction(about_action)

    def _clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.bmi_result_label.setText("BMI: ")
        self.status_label.setText("Status: ")

    def _show_usage_info(self):
        info = """
        How to Use the BMI Calculator:

        1. Enter your weight in kilograms (kg) in the 'Weight (kg)' field.
        2. Enter your height in meters (m) in the 'Height (m)' field.
        3. Click the 'Calculate BMI' button.
        4. The calculated BMI and your BMI status will be displayed below the button.

        BMI Status Guidelines (Department of Health and Human Services/NIH):
        - Underweight: less than 18.5
        - Normal: between 18.5 and 25
        - Overweight: between 25 and 30
        - Obese: 30 or greater
        """
        QMessageBox.information(self, "BMI Calculator Usage", info)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())

            if height <= 0:
                QMessageBox.critical(self, "Error", "Height must be greater than zero.")
                return

            bmi = weight / (height ** 2)
            self.bmi_result_label.setText(f"BMI: {bmi:.2f}")
            self.display_status(bmi)

        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter valid numeric values for weight and height.")

    def display_status(self, bmi):
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 25:
            status = "Normal"
        elif 25 <= bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"
        self.status_label.setText(f"Status: {status}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bmi_calculator = BMICalculator()
    bmi_calculator.show()
    sys.exit(app.exec_())