import sys
import numpy as np
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox, QStackedWidget
from PyQt5.QtGui import  QPainter, QPixmap
from PyQt5.QtCore import Qt

class LoginScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # Center the layout

        # Username input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setFixedHeight(40)
        self.username_input.setFixedWidth(300)  # Set width for consistency

        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(40)
        self.password_input.setFixedWidth(300)

        # Modern styling for the input fields
        input_style = """
        QLineEdit {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #ccc;
            background: white;
        }
        QComboBox {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #ccc;
            background: white;
        }
        """

        self.username_input.setStyleSheet(input_style)
        self.password_input.setStyleSheet(input_style)

        # Login button
        login_button = QPushButton("Login", self)
        login_button.setFixedHeight(40)
        login_button.setFixedWidth(300)
        login_button.clicked.connect(self.login)
        login_button.setStyleSheet("""
        QPushButton {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            color: white;
            border: none;
            background: #4CAF50;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        """)

        label = QLabel("Login")
        label.setStyleSheet("font-size: 30px; color: black; background: transparent;")
        # Add widgets to layout
        layout.addWidget(label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)
        layout.addStretch()
        layout.setContentsMargins(800,100,0,0)

        
        # Set layout
        self.setLayout(layout)

        self.setStyleSheet("background-image: url('background.jpg'); background-position: center; background-repeat: no-repeat;");
    def paintEvent(self, event):
        # Paint the background image
        painter = QPainter(self)
        pixmap = QPixmap('background.jpg')
        painter.drawPixmap(self.rect(), pixmap)  # Draw the image in the widget's rectangle
        super().paintEvent(event)  # Call the base class paint event to make sure other UI elements are painted properly.
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # For simplicity, we're using hardcoded login credentials
        if username == "admin" and password == "password":
            self.parent.show_dashboard()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")


class DashboardScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # Center the layout

        # Dashboard title
        title = QLabel("Dashboard")
        title.setStyleSheet("font-size: 40px;background:transparent")
        layout.addWidget(title)

        # Button to navigate to the Malnutrition Prediction app
        prediction_button = QPushButton("Malnutrition Prediction", self)
        prediction_button.setFixedHeight(40)
        prediction_button.setFixedWidth(300)
        prediction_button.clicked.connect(self.parent.show_prediction_screen)
        prediction_button.setStyleSheet("""
        QPushButton {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            background: #4CAF50;
            color: white;
            border: none;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        """)

        about_label = QLabel("Project by:\nAmeesha Thashildar\n Manasa Veeresh\n Pooja S\n Pravallika\n SDM Institute of Technology")
        about_label.setStyleSheet("font-size:20px;background: transparent")
        # Add button to layout
        layout.addWidget(prediction_button)
        layout.addWidget(about_label)
        layout.setSpacing(300)
        layout.addStretch()
    
        # Set layout
        self.setLayout(layout)
        self.setStyleSheet("background-image: url('unicef.jpg'); background-position: center; background-repeat: no-repeat;");
    
    def paintEvent(self, event):
        # Paint the background image
        painter = QPainter(self)
        pixmap = QPixmap('unicef.jpg')
        painter.drawPixmap(self.rect(), pixmap)  # Draw the image in the widget's rectangle
        super().paintEvent(event)  # Call the base class paint event to make sure other UI elements are painted properly.


class MalnutritionAppScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        # Form layout for the input fields
        form_layout = QFormLayout()

        # Create input fields
        self.patient_id_input = QLineEdit(self)
        self.height_input = QLineEdit(self)
        self.weight_input = QLineEdit(self)
        self.age_input = QLineEdit(self)

        self.sex_input = QComboBox(self)
        self.sex_input.addItem("Male")
        self.sex_input.addItem("Female")

         # Modern styling for the input fields
        input_style = """
        QLineEdit {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #ccc;
        }
        QComboBox {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #ccc;
        }
        """
        self.patient_id_input.setStyleSheet(input_style)
        self.height_input.setStyleSheet(input_style)
        self.weight_input.setStyleSheet(input_style)
        self.age_input.setStyleSheet(input_style)
        self.sex_input.setStyleSheet(input_style)

        # Model selection dropdown
        self.model_selector = QComboBox(self)
        self.model_selector.addItem("Random Forest")
        self.model_selector.addItem("Naive Bayes")
        self.model_selector.addItem("K-Nearest Neighbors")

        self.model_selector.setStyleSheet(input_style)

        # Add input fields to the form layout
        form_layout.addRow("Patient ID:", self.patient_id_input)
        form_layout.addRow("Height (cm):", self.height_input)
        form_layout.addRow("Weight (kg):", self.weight_input)
        form_layout.addRow("Age:", self.age_input)
        form_layout.addRow("Sex:", self.sex_input)
        form_layout.addRow("ML Model:", self.model_selector)

        # Diagnose button
        diagnose_button = QPushButton('Diagnose', self)
        diagnose_button.clicked.connect(self.diagnose)
        diagnose_button.setStyleSheet("""
        QPushButton {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            background-color: #4CAF50;
            color: white;
            border: none;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        """)

        # Prediction result display
        self.result_label = QLabel("Prediction: ", self)
        self.accuracy_label = QLabel("Accuracy: ", self)
        self.result_label.setMargin(30)
        self.accuracy_label.setMargin(30)
        result_style = ("font-size:25px")

        self.result_label.setStyleSheet(result_style)
        self.accuracy_label.setStyleSheet(result_style)

        # Layout for the central widget
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(diagnose_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.accuracy_label)
        layout.addStretch()

        self.setLayout(layout)

    def diagnose(self):
        try:
            # Get input values
            patient_id = self.patient_id_input.text()
            height = float(self.height_input.text())
            weight = float(self.weight_input.text())
            age = int(self.age_input.text())
            sex = 1 if self.sex_input.currentIndex() == 1 else 0  # Male=0, Female=1

            # Prepare input data
            input_data = np.array([[height, weight, age, sex]])

            accuracy = ''
            # Get the selected model
            model_name = self.model_selector.currentText()
            if model_name == "Random Forest":
                model = self.parent.rf_model
                accuracy = "78.17%"
            elif model_name == "Naive Bayes":
                model = self.parent.nb_model
                accuracy = "83.00"
            elif model_name == "K-Nearest Neighbors":
                model = self.parent.knn_model
                accuracy = "80.00"

            # Make prediction
            prediction = model.predict(input_data)[0]

            # Display the result
            self.result_label.setText(f"Prediction: {prediction}")
            self.accuracy_label.setText(f"Accuracy: {accuracy}")
            
            log = f'PatientID: {patient_id} - age: {age} - sex: {sex} - height: {height} - weight: {weight} - Model: {model_name} - Prediction: {prediction}'                                                                                                                                                                                                                                                                                                                                                 
            self.save_log(log)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
    
    def save_log(self, data):
        log_file = "records.txt"  # The name of the log file
        with open(log_file, 'a') as file:  # Open file in append mode
            file.write(f"record: {data}\n")  # Append the log entry to the file



class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load models
        self.rf_model = pickle.load(open("Models/rf_model.pkl", "rb"))
        self.nb_model = pickle.load(open("Models/nb_model.pkl", "rb"))
        self.knn_model = pickle.load(open("Models/knn_model.pkl", "rb"))

        # Initialize the main window
        self.setWindowTitle('Malnutrition Prediction App')
        self.setGeometry(100, 100, 1600, 900)

        # Create the stacked widget for switching screens
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Create and add the screens to the stacked widget
        self.login_screen = LoginScreen(self)
        self.dashboard_screen = DashboardScreen(self)
        self.prediction_screen = MalnutritionAppScreen(self)

        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.dashboard_screen)
        self.stacked_widget.addWidget(self.prediction_screen)

        # Show the login screen initially
        self.stacked_widget.setCurrentWidget(self.login_screen)

    def show_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.dashboard_screen)

    def show_prediction_screen(self):
        self.stacked_widget.setCurrentWidget(self.prediction_screen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
