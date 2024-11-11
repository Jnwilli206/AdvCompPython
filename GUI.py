#Imports PyQt6 and multiple different modules for it.
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

#class Window is used to create a gui window for inputing text and displaying it in the console.
class Window(QWidget):
    def __init__(this):
        super().__init__() 
        this.setWindowTitle("BlingoBlongo") #sets the title of the window
        this.resize(250, 100) #sets the size of the window
    
        layout = QVBoxLayout() #sets the var layout as QVBoxLayout
        this.setLayout(layout) #sets the layout of the window to the var layout


        submit_button = QPushButton("Submit") #creates a submit button
        submit_button.clicked.connect(this.submit_text) #makes it so when the button is clicked it submits text
        layout.addWidget(submit_button) #adds the submit button to the layout

        this.input = QLineEdit() #creates an input line
        this.input.setPlaceholderText("Enter text...") #sets what text is inside the input line before text is entered
        layout.addWidget(this.input) #adds the input line to the layout
        
    def submit_text(this): #defines submit text which is the function that saves text inputed and displays it in the console
        text = this.input.text()
        print(f"{text} is what you submitted!")

app = QApplication(sys.argv) #creates the app that will be opened when accessing the gui
window = Window() #assigns a Window object to window
window.show() #shows the window
sys.exit(app.exec()) #exits the system if the app is exited
