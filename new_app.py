import sys
import os

import random

import json
import re
import numpy as np
import pandas as pd

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtCore import Qt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pickle

from window import Ui_MalnutritionApp

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MalnutritionApp()
        self.ui.setupUi(self)

        self.init_ui()
        self.make_connections()

        self.load_models()
        self.load_database()
        self.load_records()
    
    def load_models(self):
        self.rf_model = pickle.load(open("Models/rf_model.pkl", "rb"))
        self.nb_model = pickle.load(open("Models/nb_model.pkl", "rb"))
        self.knn_model = pickle.load(open("Models/knn_model.pkl", "rb"))
        self.nn_model = pickle.load(open("Models/nn_model.pkl", "rb"))
        self.LR_model = pickle.load(open("Models/LR.pkl", "rb"))

    def init_ui(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.sexInput.addItems(['Male', 'Female'])
        self.ui.modelInput.addItems(['NaiveBayes', 'RandomForest', 'KNearestNeighbors', 'NeuralNetwork', 'LogisticRegression'])
        self.ui.comboBox.addItems(['Sr. Doctor', 'Doctor', 'Jr. Doctor', 'Nutritionist', 'Dietician', 'Nurse'])

        int_validator = QIntValidator(self)
        float_validator = QDoubleValidator(self)

        self.ui.patientIDInput.setValidator(int_validator)
        self.ui.AgeInput.setValidator(int_validator)
        self.ui.heightInput.setValidator(float_validator)
        self.ui.WeightInput.setValidator(float_validator)
        self.ui.nameInput_4.setValidator(int_validator)

        self.ui.resultLabel.setText('Prediction: ')
        self.ui.nutrtionbtn.setVisible(False)

        self.ui.ERRORLABEL.setStyleSheet('font-size:25px;')

        self.graph = MLParameterGraph()
        layout = self.ui.graphwidget.layout()  # Assuming you've added a layout
        if layout:
            layout.addWidget(self.graph)
        else:
            self.ui.graphwidget.setLayout(QVBoxLayout())
            self.ui.graphwidget.layout().addWidget(self.graph)

    def make_connections(self):
        self.ui.loginBtn.clicked.connect(self.loginBtnClicked)
        self.ui.predictBtn.clicked.connect(self.predictClicked)
        self.ui.ModelBackBtn_3.clicked.connect(self.registerClicked)
        self.ui.nutrtionbtn.clicked.connect(self.open_diet_page)
        self.ui.dashboardLogoutBtn.clicked.connect(self.logoutClicked)
        
        self.ui.dietBackBtn.clicked.connect(self.page_backbtnClicked)
        self.ui.ModelBackBtn.clicked.connect(self.page_backbtnClicked)
        self.ui.backBtn.clicked.connect(self.page_backbtnClicked)
        self.ui.backBtn_2.clicked.connect(self.page_backbtnClicked)
        self.ui.backBtn2.clicked.connect(self.page_backbtnClicked)
        self.ui.RegisterBackBtn.clicked.connect(self.page_backbtnClicked)
        self.ui.aboutbackBtn.clicked.connect(self.page_backbtnClicked)
        self.ui.graphbackbtn.clicked.connect(self.page_backbtnClicked)
        
        self.ui.dashboardPredictionBtn.clicked.connect(self.open_prediction_page)
        self.ui.dashboardAboutBtn.clicked.connect(self.open_about_page)
        self.ui.dashboardDietBtn.clicked.connect(self.open_diet_page)
        self.ui.dashboardModelsBtn.clicked.connect(self.open_models_page)
        self.ui.dashboardRecordsBtn.clicked.connect(self.open_records_page)
        self.ui.dashboardRegisterBtn.clicked.connect(self.open_registration_page)
        self.ui.dashboardScaleBtn.clicked.connect(self.open_scale_page)
        self.ui.dashboardDataBtn.clicked.connect(self.open_graph_page)

        """
        0 - loginpage
        1 - dashboard
        2 - predict
        3 - scale
        4 - records
        5 - diet
        6 - models
        7 - registration
        8 - about
        """
    
    def load_database(self):
        with open('users.json', 'r') as file:
            self.user_data = json.load(file)
    
        self.user_map = self.user_data["USERS"]

    def open_scale_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def open_registration_page(self):
        self.ui.stackedWidget.setCurrentIndex(7)
        self.ui.nameInput.setText('')
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.nameInput_4.setText('')
        self.ui.nameInput_3.setText('')
        self.ui.nameInput_8.setText('')
        self.ui.nameInput_2.setText('')
        self.ui.ERRORLABEL.setText('')
    
    def open_records_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.load_records()

    def open_models_page(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    
    def open_diet_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def open_about_page(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def open_prediction_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

        self.ui.patientIDInput.setText('')
        self.ui.heightInput.setText('')
        self.ui.WeightInput.setText('')
        self.ui.AgeInput.setText('')
        self.ui.sexInput.setCurrentIndex(0)
        self.ui.modelInput.setCurrentIndex(0)
        self.ui.resultLabel.setText('Prediction: ')
        self.ui.accuracyLabel.setText('Accuracy: ')
        self.ui.resultLabel.setStyleSheet('color:white;')

        self.ui.nutrtionbtn.setVisible(False)
    
    def page_backbtnClicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def logoutClicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def open_graph_page(self):
        self.ui.stackedWidget.setCurrentIndex(9)
        self.load_records()
        self.graph.update_data(self.graphdata)


    def registerClicked(self):
        if (self.ui.nameInput.text() == '' or
            self.ui.nameInput_4.text() == '' or
            self.ui.nameInput_3.text() == '' or
            self.ui.nameInput_8.text() == '' or
            self.ui.nameInput_2.text() == ''
        ):
            self.ui.ERRORLABEL.setText('One or More Input Fields are Empty. Please Check!')
            self.ui.ERRORLABEL.setStyleSheet('color:red;')
            return
        self.ui.ERRORLABEL.setText('')

        full_name = self.ui.nameInput.text()
        title = self.ui.comboBox.currentText()
        number = self.ui.nameInput_4.text()
        email = self.ui.nameInput_3.text()
        username = self.ui.nameInput_8.text()
        pswd = self.ui.nameInput_2.text()

        try:
            self.user_data["USERS"][username]
            self.ui.ERRORLABEL.setText('UserName Already Exist!')
            self.ui.ERRORLABEL.setStyleSheet('color:red;')
            return
        except KeyError:
            pass

        self.ui.ERRORLABEL.setText('Registration Successful!')
        self.ui.ERRORLABEL.setStyleSheet('color:rgb(52, 255, 86;font-size: 20px;')

        self.user_data["USERS"][username] = {
                                            "name" : full_name,
                                            "Title" : title,
                                            "Pswd" : pswd,
                                            "Mobile" : number,
                                            "email" : email
                                                        }

        json_data = json.dumps(self.user_data,indent=4)

        with open('users.json', 'w') as file:
            file.write(json_data)

        self.load_database()
    
    def loginBtnClicked(self):
        if self.ui.userInput.text == '' or self.ui.pswdInput.text == '':
            QMessageBox.warning(None, "Login Failed", "Please Enter Details")
        
        userid = self.ui.userInput.text()
        pswd = self.ui.pswdInput.text()

        try:
            if self.user_map[userid]["Pswd"] == pswd:
                self.ui.userInput.setText('')
                self.ui.pswdInput.setText('')
                self.ui.usernamelabel.setText(self.user_map[userid]["name"])
                self.page_backbtnClicked()
            else:
                QMessageBox.warning(None, "Login Failed", "Incorrect password! Try Again")
        except KeyError:
            QMessageBox.warning(None, "Login Failed", "User Not Found! Try Again")

    def predictClicked(self):
        try:
            if (
                self.ui.patientIDInput.text() == '' or
                self.ui.heightInput.text() == '' or
                self.ui.WeightInput.text() == '' or
                self.ui.AgeInput.text() == '' or
                self.ui.sexInput.currentText() == '' or
                self.ui.modelInput.currentText() == ''
            ):
                QMessageBox.warning(None, "Error", "One or More Inputs Fields Cannot be Empty! Please Check the Data")

            patient_id = self.ui.patientIDInput.text()
            height = float(self.ui.heightInput.text())
            weight = float(self.ui.WeightInput.text())
            age = int(self.ui.AgeInput.text())
            sex = 1 if self.ui.sexInput.currentIndex() == 1 else 0  # Male=0, Female=1

            # Prepare input data
            input_data = pd.DataFrame({     "Sex": [sex],
                                            "Age": [age],
                                            "Height": [height],
                                            "Weight": [weight]
                                        })
            
            accuracy = ''
            # Get the selected model
            model_name = self.ui.modelInput.currentText()
            if model_name == "RandomForest":
                model = self.rf_model
                accuracy = "78.17%"
            elif model_name == "NaiveBayes":
                model = self.nb_model
                accuracy = "83.00"
            elif model_name == "KNearestNeighbors":
                model = self.knn_model
                accuracy = "80.00"
            elif model_name == 'NeuralNetwork':
                model = self.nn_model
                accuracy = "98.78"
            elif model_name == 'LogisticRegression':
                model = self.LR_model
                accuracy = '85.45'

            # Make prediction
            prediction = model.predict(input_data)[0]

            # Display the result
            if prediction in ['Stunting', 'Wasting']:
                self.ui.resultLabel.setStyleSheet('color: red;')
            elif prediction in ['Overweight', 'Underweight']:
                self.ui.resultLabel.setStyleSheet('color: orange;')

            self.ui.resultLabel.setText(f"Prediction: {prediction}")
            self.ui.accuracyLabel.setText(f"Accuracy: {accuracy}")

            self.ui.nutrtionbtn.setVisible(True)

            sex = 'Male' if sex == 0 else 'Female'

            log = f'PatientID: {patient_id} - height: {height} - weight: {weight} - age: {age} - sex: {sex} - Model: {model_name} - Prediction: {prediction}'                                                                                                                                                                                                                                                                                                                                                 
            self.save_log(log)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")
    
    def save_log(self, log):
        log_file = "records.txt"  # The name of the log file
        with open(log_file, 'a') as file:  # Open file in append mode
            file.write(f"{log}\n")  # Append the log entry to the file
    
    def load_records(self):
        # File path to your text file containing the records
        file_path = "records.txt"
        self.graphdata = []

        try:
            self.ui.tableWidget.setRowCount(0)
            with open(file_path, "r") as file:
                # Read all lines from the file
                lines = file.readlines()

                models = ['NaiveBayes', 'KNearestNeighbors', 'RandomForest', 'NeuralNetwork', 'LogisticRegression']
                # Insert rows and set data for each record
                for line in lines:
                    # Regular expression to extract key-value pairs from the line
                    record = re.findall(r'(\w+):\s*([\w\.]+)', line.strip())

                    if len(record) == 7:  # Ensure it has exactly 6 key-value pairs
                        current_row = self.ui.tableWidget.rowCount()
                        self.ui.tableWidget.insertRow(current_row)

                        # Set data for each column
                        data = {}
                        for i, (key, value) in enumerate(record):
                            self.ui.tableWidget.setItem(current_row, i, QTableWidgetItem(value))
                            data[key] = value

                        del data['PatientID']
                        del data['Prediction']
                        data['height'] = float(data['height'])
                        data['weight'] = float(data['weight'])
                        data['age'] = int(data['age'])
                        data['Model'] = models.index(data['Model'])
                        self.graphdata.append(data)

        except FileNotFoundError:
            print(f"File '{file_path}' not found.")

class MLParameterGraph(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Main Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Graph Canvas
        self.figure = Figure(figsize=(30, 10))
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Legend Widget
        self.legend_label = QLabel()
        self.legend_label.setStyleSheet("font-size:15px;color:black;font-weight:bold;background-color:white;")
        self.legend_label.setAlignment(Qt.AlignLeft)
        self.legend_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.legend_label)

        # Data Storage
        self.data = pd.DataFrame(columns=["height", "weight", "age", "sex", "Model"])

    def update_data(self, new_data):
        """Update with new prediction data."""
        self.data = pd.concat([self.data, pd.DataFrame(new_data)], ignore_index=True)
        self.plot_graph()

    def plot_graph(self):
        """Plot the custom graph."""
        self.figure.clear()

        # Adjust figure margins to fit the legend
        self.figure.subplots_adjust(bottom=0.3, wspace=0.3)

        # Subplots
        ax1 = self.figure.add_subplot(131)  # Parameter Distribution
        ax2 = self.figure.add_subplot(132)  # Model Usage Frequency
        ax3 = self.figure.add_subplot(133)  # Scatter Plot

        # 1. Parameter Distribution by Model
        if not self.data.empty:
            for i, param in enumerate(["height", "weight", "age"]):
                grouped = self.data.groupby("Model")[param]
                labels = grouped.groups.keys()
                values = [grouped.get_group(label).values for label in labels]
                ax1.boxplot(values, labels=labels)
                ax1.set_title(f"Distribution of {param}")
                ax1.set_xlabel("Model")
                ax1.set_ylabel(param)

        # 2. Model Usage Frequency
        model_counts = self.data["Model"].value_counts()
        ax2.bar(model_counts.index, model_counts.values, color="skyblue")
        ax2.set_title("Model Usage Frequency")
        ax2.set_xlabel("Model")
        ax2.set_ylabel("Count")

        # 3. Scatter Plot (Height vs. Weight)
        if "height" in self.data and "weight" in self.data:
            for model in self.data["Model"].unique():
                subset = self.data[self.data["Model"] == model]
                ax3.scatter(subset["height"], subset["weight"], label=model, alpha=0.6)
            ax3.set_title("Height vs Weight")
            ax3.set_xlabel("Height")
            ax3.set_ylabel("Weight")
            ax3.legend(title="Model")

        # Update Legend Text
        legend_labels = [
            '1: Naive Bayes',
            '2: K Nearest Neighbors',
            '3: Random Forest',
            '4: Neural Network',
            '5: Logistic Regression'
        ]
        self.legend_label.setText("\n".join(legend_labels))

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainApp()
    
    main_window.show()
    sys.exit(app.exec())

