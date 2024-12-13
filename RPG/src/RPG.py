#Goals
#Make the game entirely playable through a gui of buttons and pictures
#Use random, data structures, and most everything we've learned.
#Have a full dungeon with branching paths, maybe even randomly shuffle the rooms.
#Have enemies to fight and challenges to overcome.
#Have loot that changes various stats, and make it realistic in what you can actually carry

#Starting variables for the player character. Maybe can add multiple classes with diff stats.

#Imports PyQt6 and multiple different modules for it.
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QPixmap

#Sets variables for having certain items to false, when gained they are set to true.
hasBone = False
hasGold = False
hasGhostBlade = False
hasKey = False

#Function that clears the gui
def ClearBoard():
    Game.RestartButton.setVisible(False)

    Game.Slide1ImageLabel.setVisible(False)
    Game.Slide2ImageLabel.setVisible(False)
    Game.Slide3ImageLabel.setVisible(False)
    Game.Slide4ImageLabel.setVisible(False)
    Game.Slide5ImageLabel.setVisible(False)
    Game.Slide6ImageLabel.setVisible(False)
    Game.Slide7ImageLabel.setVisible(False)
    Game.Slide8ImageLabel.setVisible(False)
    Game.Slide9ImageLabel.setVisible(False)
    Game.Slide10ImageLabel.setVisible(False)

    Game.Slide1label1.setVisible(False)
    Game.Slide1label2.setVisible(False)
    Game.Slide1label3.setVisible(False)
    Game.Slide1label4.setVisible(False)
    Game.Slide2label1.setVisible(False)
    Game.Slide2label2.setVisible(False)
    Game.Slide2label3.setVisible(False)
    Game.Slide2label4.setVisible(False)
    Game.Slide3label1.setVisible(False)
    Game.Slide3label2.setVisible(False)
    Game.Slide3label3.setVisible(False)
    Game.Slide3label4.setVisible(False)
    Game.Slide3label5.setVisible(False)
    Game.Slide3label6.setVisible(False)
    Game.Slide3label7.setVisible(False)

    Game.Slide4label1.setVisible(False)
    Game.Slide4label2.setVisible(False)
    Game.Slide4label3.setVisible(False)
    Game.Slide4label4.setVisible(False)
    Game.Slide4label5.setVisible(False)
    Game.Slide4label6.setVisible(False)
    
    Game.Slide5label1.setVisible(False)
    Game.Slide5label2.setVisible(False)
    Game.Slide5label3.setVisible(False)
    Game.Slide5label4.setVisible(False)
    Game.Slide5label5.setVisible(False)
    Game.Slide5label6.setVisible(False)
    Game.Slide5label7.setVisible(False)
    Game.Slide5label8.setVisible(False)

    Game.Slide6label1.setVisible(False)
    Game.Slide6label2.setVisible(False)
    Game.Slide6label3.setVisible(False)
    Game.Slide6label4.setVisible(False)

    Game.Slide7label1.setVisible(False)
    Game.Slide7label2.setVisible(False)
    Game.Slide7label3.setVisible(False)
    Game.Slide7label4.setVisible(False)
    Game.Slide7label5.setVisible(False)
    Game.Slide7label6.setVisible(False)

    Game.Slide8label1.setVisible(False)
    Game.Slide8label2.setVisible(False)
    Game.Slide8label3.setVisible(False)
    Game.Slide8label4.setVisible(False)
    Game.Slide8label5.setVisible(False)

    Game.Slide9label1.setVisible(False)
    Game.Slide9label2.setVisible(False)
    Game.Slide9label3.setVisible(False)
    Game.Slide9label4.setVisible(False)
    Game.Slide9label5.setVisible(False)
    Game.Slide9label6.setVisible(False)
    Game.Slide9label7.setVisible(False)
    Game.Slide9label8.setVisible(False)
    Game.Slide9label9.setVisible(False)

    Game.Slide10label1.setVisible(False)
    Game.Slide10label2.setVisible(False)
    Game.Slide10label3.setVisible(False)
    Game.Slide10label4.setVisible(False)
    Game.Slide10label5.setVisible(False)
    Game.Slide10label6.setVisible(False)
    Game.Slide10label7.setVisible(False)
    Game.Slide10label8.setVisible(False)
    Game.Slide10label9.setVisible(False)
    
    Game.Slide1Button1.setVisible(False)
    
    Game.Slide2Button1.setVisible(False)
    Game.Slide2Button2.setVisible(False)
    
    Game.Slide3Button1.setVisible(False)
    Game.Slide3Button2.setVisible(False)
    Game.Slide3Button3.setVisible(False)
    Game.Slide3Button4.setVisible(False)

    Game.Slide4Button1.setVisible(False)
    Game.Slide4Button2.setVisible(False)
    Game.Slide4Button3.setVisible(False)
    Game.Slide4Button4.setVisible(False)

    Game.Slide5Button1.setVisible(False)
    Game.Slide5Button2.setVisible(False)
    Game.Slide5Button3.setVisible(False)
    Game.Slide5Button4.setVisible(False)

    Game.Slide6Button1.setVisible(False)
    Game.Slide6Button2.setVisible(False)
    Game.Slide6Button3.setVisible(False)

    Game.Slide7Button1.setVisible(False)
    Game.Slide7Button2.setVisible(False)
    Game.Slide7Button3.setVisible(False)
    Game.Slide7Button4.setVisible(False)
    Game.Slide7Button5.setVisible(False)

    Game.Slide8Button1.setVisible(False)
    Game.Slide8Button2.setVisible(False)
    Game.Slide8Button3.setVisible(False)
    Game.Slide8Button4.setVisible(False)

    Game.Slide9Button1.setVisible(False)
    Game.Slide9Button2.setVisible(False)
    Game.Slide9Button3.setVisible(False)
    Game.Slide9Button4.setVisible(False)
    Game.Slide9Button5.setVisible(False)

    Game.Slide10Button1.setVisible(False)
    Game.Slide10Button2.setVisible(False)
    Game.Slide10Button3.setVisible(False)
    Game.Slide10Button4.setVisible(False)



#Restart to slide 1 function
def Restart():
    ClearBoard()
    global hasBone
    hasBone = False
    global hasGold
    hasGold = False
    global hasGhostBlade
    hasGhostBlade = False
    global hasKey
    hasKey = False

    Game.Slide1ImageLabel.setVisible(True)

    Game.Slide1label1.setVisible(True)
    Game.Slide1label2.setVisible(True)
    Game.Slide1label3.setVisible(True)
    Game.Slide1label4.setVisible(True)

    Game.Slide1Button1.setVisible(True)

#Sets Slide 2 to visible
def Slide2SetVis():
    ClearBoard()

    Game.Slide2ImageLabel.setVisible(True)

    Game.Slide2label1.setVisible(True)
    Game.Slide2label2.setVisible(True)
    Game.Slide2label3.setVisible(True)
    Game.Slide2label4.setVisible(True)

    Game.Slide2Button1.setVisible(True)
    Game.Slide2Button2.setVisible(True)

#Sets Slide 3 to visible
def Slide3SetVis():
    ClearBoard()

    Game.Slide3ImageLabel.setVisible(True)

    Game.Slide3label1.setVisible(True)
    Game.Slide3label2.setVisible(True)
    Game.Slide3label3.setVisible(True)
    Game.Slide3label4.setVisible(True)

    Game.Slide3Button1.setVisible(True)
    Game.Slide3Button2.setVisible(True)
    Game.Slide3Button3.setVisible(True)

#Sets Slide 3p1 to visible
def Slide3p1SetVis():
    ClearBoard()

    Game.Slide3ImageLabel.setVisible(True)

    Game.Slide3label5.setVisible(True)

    Game.Slide3Button4.setVisible(True)
    global hasBone
    hasBone = True #Player gains bone

#Sets slide 3p2 to visible
def Slide3p2SetVis():
    ClearBoard()

    Game.Slide3ImageLabel.setVisible(True)

    Game.Slide3label6.setVisible(True)

    Game.Slide3Button4.setVisible(True)

#Sets slide 3p3 to visible
def Slide3p3SetVis():
    ClearBoard()

    Game.Slide3ImageLabel.setVisible(True)

    Game.Slide3label7.setVisible(True)

    Game.RestartButton.setVisible(True)

#Sets Slide 4 to visible
def Slide4SetVis():
    ClearBoard()

    Game.Slide4ImageLabel.setVisible(True)

    Game.Slide4label1.setVisible(True)
    Game.Slide4label2.setVisible(True)
    Game.Slide4label3.setVisible(True)
    Game.Slide4label4.setVisible(True)

    Game.Slide4Button1.setVisible(True)
    Game.Slide4Button2.setVisible(True)
    Game.Slide4Button3.setVisible(True)

#Sets Slide 4p1 to visible
def Slide4p1SetVis():
    ClearBoard()
    global hasGold
    hasGold = True
    Game.Slide4ImageLabel.setVisible(True)

    Game.Slide4label5.setVisible(True)

    Game.Slide4Button4.setVisible(True)

#Sets Slide 4p2 to visible
def Slide4p2SetVis():
    ClearBoard()
    Game.Slide4ImageLabel.setVisible(True)

    Game.Slide4label6.setVisible(True)

    Game.Slide4Button4.setVisible(True)

#Sets Slide 5 to visible
def Slide5SetVis():
    ClearBoard()
    Game.Slide5ImageLabel.setVisible(True)

    Game.Slide5label1.setVisible(True)
    Game.Slide5label2.setVisible(True)
    Game.Slide5label3.setVisible(True)
    Game.Slide5label4.setVisible(True)

    Game.Slide5Button1.setVisible(True)
    Game.Slide5Button2.setVisible(True)
    Game.Slide5Button3.setVisible(True)

#Sets Slide 5p1 to visible
def Slide5p1SetVis():
    ClearBoard()
    Game.Slide5ImageLabel.setVisible(True)

    Game.Slide5label5.setVisible(True)
    Game.Slide5label6.setVisible(True)

    Game.RestartButton.setVisible(True)

#Sets Slide 5p2 to visible
def Slide5p2SetVis():
    ClearBoard()
    global hasKey
    hasKey = True
    Game.Slide5ImageLabel.setVisible(True)

    Game.Slide5label7.setVisible(True)
    Game.Slide5label8.setVisible(True)

    Game.Slide5Button4.setVisible(True)

#Sets Slide 6 to visible
def Slide6SetVis():
    ClearBoard()
    Game.Slide6ImageLabel.setVisible(True)

    Game.Slide6label1.setVisible(True)
    Game.Slide6label2.setVisible(True)
    Game.Slide6label3.setVisible(True)
    Game.Slide6label4.setVisible(True)

    Game.Slide6Button1.setVisible(True)
    Game.Slide6Button2.setVisible(True)
    Game.Slide6Button3.setVisible(True)

#Sets Slide 7 to visible
def Slide7SetVis():
    ClearBoard()
    global hasBone
    global hasGhostBlade
    Game.Slide7ImageLabel.setVisible(True)

    Game.Slide7label1.setVisible(True)
    Game.Slide7label2.setVisible(True)
    Game.Slide7label3.setVisible(True)

    Game.Slide7Button1.setVisible(True)
    Game.Slide7Button2.setVisible(True)
    if (hasBone):
        Game.Slide7Button3.setVisible(True)
    if (hasGhostBlade):
        Game.Slide7Button4.setVisible(True) 

#Sets Slide 7p1 to visible
def Slide7p1SetVis():
    ClearBoard()
    Game.Slide7ImageLabel.setVisible(True)

    Game.Slide7label4.setVisible(True)

    Game.RestartButton.setVisible(True) 

#Sets Slide 7p2 to visible
def Slide7p2SetVis():
    ClearBoard()
    Game.Slide7ImageLabel.setVisible(True)

    Game.Slide7label5.setVisible(True)

    Game.Slide7Button5.setVisible(True) 

#Sets Slide 7p3 to visible
def Slide7p3SetVis():
    ClearBoard()
    Game.Slide7ImageLabel.setVisible(True)

    Game.Slide7label6.setVisible(True)

    Game.Slide7Button5.setVisible(True)

#Sets Slide 8 to visible
def Slide8SetVis():
    ClearBoard()
    Game.Slide8ImageLabel.setVisible(True)

    Game.Slide8label1.setVisible(True)
    Game.Slide8label2.setVisible(True)
    Game.Slide8label3.setVisible(True)

    Game.Slide8Button1.setVisible(True)
    Game.Slide8Button2.setVisible(True)
    Game.Slide8Button3.setVisible(True)

#Sets Slide 8p1 to visible
def Slide8p1SetVis():
    ClearBoard()
    Game.Slide8ImageLabel.setVisible(True)

    Game.Slide8label4.setVisible(True)

    Game.RestartButton.setVisible(True)

def Slide8p2SetVis():
    ClearBoard()
    global hasGhostBlade
    hasGhostBlade = True
    Game.Slide8ImageLabel.setVisible(True)

    Game.Slide8label5.setVisible(True)

    Game.Slide8Button4.setVisible(True)

def Slide9SetVis():
    ClearBoard()
    global hasKey
    global hasGold
    global hasGhostBlade
    Game.Slide9ImageLabel.setVisible(True)

    Game.Slide9label1.setVisible(True)
    Game.Slide9label2.setVisible(True)
    Game.Slide9label3.setVisible(True)
    Game.Slide9label4.setVisible(True)

    Game.Slide9Button1.setVisible(True)

    if(hasKey):
        Game.Slide9Button2.setVisible(True)
    if(hasGhostBlade):
        Game.Slide9Button3.setVisible(True)
    if(hasGold):
        Game.Slide9Button4.setVisible(True)

def Slide9p1SetVis():
    ClearBoard()
    global hasKey
    Game.Slide9ImageLabel.setVisible(True)

    Game.Slide9label6.setVisible(True)

    Game.RestartButton.setVisible(True)

    if(hasKey):
        Game.Slide9Button2.setVisible(True)

def Slide9p2SetVis():
    ClearBoard()
    Game.Slide9ImageLabel.setVisible(True)

    Game.Slide9label8.setVisible(True)
    Game.Slide9label9.setVisible(True)

    Game.Slide9Button5.setVisible(True)

def Slide9p3SetVis():
    ClearBoard()
    Game.Slide9ImageLabel.setVisible(True)

    Game.Slide9label7.setVisible(True)
    Game.Slide9label9.setVisible(True)

    Game.Slide9Button5.setVisible(True)

def Slide9p4SetVis():
    ClearBoard()
    global hasGold 
    hasGold = False
    Game.Slide9ImageLabel.setVisible(True)

    Game.Slide9label5.setVisible(True)
    Game.Slide9label9.setVisible(True)

    Game.Slide9Button5.setVisible(True)

def Slide10SetVis():
    ClearBoard()
    global hasGold
    global hasGhostBlade
    Game.Slide10ImageLabel.setVisible(True)

    Game.Slide10label1.setVisible(True)
    Game.Slide10label2.setVisible(True)
    Game.Slide10label3.setVisible(True)
    Game.Slide10label4.setVisible(True)

    Game.Slide10Button1.setVisible(True)
    Game.Slide10Button2.setVisible(True)

    if(hasGhostBlade):
        Game.Slide10Button3.setVisible(True)
    if(hasGold):
        Game.Slide10Button4.setVisible(True)

def Slide10p1SetVis():
    ClearBoard()
    Game.Slide10ImageLabel.setVisible(True)

    Game.Slide10label5.setVisible(True)

    Game.RestartButton.setVisible(True)

def Slide10p2SetVis():
    ClearBoard()
    Game.Slide10ImageLabel.setVisible(True)

    Game.Slide10label6.setVisible(True)
    Game.Slide10label7.setVisible(True)

def Slide10p3SetVis():
    ClearBoard()
    Game.Slide10ImageLabel.setVisible(True)

    Game.Slide10label8.setVisible(True)
    Game.Slide10label9.setVisible(True)





    
#The app to use GUI
app = QApplication(sys.argv) 

#Game-------------------------------------------------------------
Game = QWidget()
Game.setStyleSheet("""
            /* General Window Styling */
            QMainWindow {
                background-color: #2d2a32;
                border: 2px solid #5a3e1b;
                border-radius: 15px;
            }

            /* Buttons */
            QPushButton {
                background-color: #7a5230;
                color: #f4e9d8;
                border: 2px solid #5a3e1b;
                border-radius: 10px;
                padding: 5px 15px;
                font-family: "Papyrus", fantasy;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #8c6747;
                border: 2px solid #a56b34;
                color: #ffebc7;
            }
            QPushButton:pressed {
                background-color: #5a3e1b;
                border: 2px solid #2d2a32;
                color: #e0c9a1;
            }

            /* Labels */
            QLabel {
                color: #d8c097;
                font-family: "Georgia", serif;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
            }

            /* Line Edit (Input) */
            QLineEdit {
                background-color: #3a3028;
                color: #f4e9d8;
                border: 2px solid #5a3e1b;
                border-radius: 5px;
                padding: 3px;
                font-family: "Georgia", serif;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #a56b34;
            }

            /* ComboBox */
            QComboBox {
                background-color: #3a3028;
                color: #f4e9d8;
                border: 2px solid #5a3e1b;
                border-radius: 5px;
                padding: 3px;
                font-family: "Georgia", serif;
                font-size: 14px;
            }
            QComboBox:hover {
                border: 2px solid #a56b34;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #3a3028;
                color: #f4e9d8;
                border: 2px solid #5a3e1b;
                selection-background-color: #5a3e1b;
                selection-color: #f4e9d8;
            }

            /* ScrollBars */
            QScrollBar:vertical {
                background: #3a3028;
                width: 10px;
                margin: 15px 3px 15px 3px;
                border: 1px solid #5a3e1b;
            }
            QScrollBar::handle:vertical {
                background: #7a5230;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: #5a3e1b;
                height: 14px;
                border-radius: 5px;
            }

            /* Checkboxes */
            QCheckBox {
                color: #d8c097;
                font-family: "Georgia", serif;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
            }
            QCheckBox::indicator:checked {
                background: #7a5230;
                border: 2px solid #a56b34;
            }

            /* Progress Bar */
            QProgressBar {
                background-color: #3a3028;
                color: #f4e9d8;
                border: 2px solid #5a3e1b;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #7a5230;
                width: 20px;
                margin: 0.5px;
            }

            /* MenuBar */
            QMenuBar {
                background-color: #3a3028;
                color: #f4e9d8;
                border: 1px solid #5a3e1b;
            }
            QMenuBar::item {
                background: transparent;
                padding: 5px 15px;
            }
            QMenuBar::item:selected {
                background: #5a3e1b;
                color: #ffebc7;
            }

            /* ToolTips */
            QToolTip {
                background-color: #5a3e1b;
                color: #f4e9d8;
                border: 1px solid #7a5230;
                padding: 5px;
                border-radius: 5px;
                font-family: "Georgia", serif;
            }
            """
        )

#Game Title and size
Game.setWindowTitle("RPG Game (text)") 
Game.resize(500, 500) 

#Game Layout
layout = QVBoxLayout() 
Game.setLayout(layout) 

#Slide1-------------------------------------------------------------
#Slide1 Image
Slide1Image = QPixmap("GameCave.png")
Game.Slide1ImageLabel = QLabel(Game)
Game.Slide1ImageLabel.setPixmap(Slide1Image)
layout.addWidget(Game.Slide1ImageLabel)

#Slide1 Text lines
Game.Slide1label1 = QLabel("In a faraway land you find yourself at the entrance to a cave.")
Game.Slide1label2 = QLabel("It is said to contain a great treasure, and a great monster who guards it.")
Game.Slide1label3 = QLabel("Will you enter?")
Game.Slide1label4 = QLabel("")
layout.addWidget(Game.Slide1label1)
layout.addWidget(Game.Slide1label2)
layout.addWidget(Game.Slide1label3)
layout.addWidget(Game.Slide1label4)


#Slide1 Buttons
Game.Slide1Button1 = QPushButton("Enter")
layout.addWidget(Game.Slide1Button1)



#Slide2-------------------------------------------------------------
#Slide2 Image
Slide3Image = QPixmap("GameSplitPath.png")
Game.Slide2ImageLabel = QLabel(Game)
Game.Slide2ImageLabel.setPixmap(Slide3Image)
layout.addWidget(Game.Slide2ImageLabel)
Game.Slide2ImageLabel.setVisible(False)

#Slide2 Text lines
Game.Slide2label1 = QLabel("You walk down the cave for a while and come to a crossroads.")
Game.Slide2label2 = QLabel("A dark dreary tunnel fitted with the smell of decay.")
Game.Slide2label3 = QLabel("A lush mossy path with a sweet aroma that fills the air.")
Game.Slide2label4 = QLabel("Which path will you tread?")
layout.addWidget(Game.Slide2label1)
Game.Slide2label1.setVisible(False)
layout.addWidget(Game.Slide2label2)
Game.Slide2label2.setVisible(False)
layout.addWidget(Game.Slide2label3)
Game.Slide2label3.setVisible(False)
layout.addWidget(Game.Slide2label4)
Game.Slide2label4.setVisible(False)


#Slide2 Buttons
Game.Slide2Button1 = QPushButton("The dark path.")
Game.Slide2Button2 = QPushButton("The mossy path.")
layout.addWidget(Game.Slide2Button1)
layout.addWidget(Game.Slide2Button2)
Game.Slide2Button1.setVisible(False)
Game.Slide2Button2.setVisible(False)

#Slide3-------------------------------------------------------------
#Slide3 Image
Slide3Image = QPixmap("GameSkeleton.png")
Game.Slide3ImageLabel = QLabel(Game)
Game.Slide3ImageLabel.setPixmap(Slide3Image)
layout.addWidget(Game.Slide3ImageLabel)
Game.Slide3ImageLabel.setVisible(False)

#Slide3 Text lines
Game.Slide3label1 = QLabel("You walk down the dark tunnel.")
Game.Slide3label2 = QLabel("Suddenly from the shadows you hear a rattle of bones.")
Game.Slide3label3 = QLabel("A bone visage comes into your torchlight, its joints creaking with every step.")
Game.Slide3label4 = QLabel("What will you do?")
Game.Slide3label5 = QLabel("You grapple the skeleton to the ground and rip out one of its rib bones. +GAINED BONE")
Game.Slide3label6 = QLabel("You slash the skeleton destroying it.")
Game.Slide3label7 = QLabel("You fail to scare the skeleton off. It lunges at you and kills you. You lose.")
layout.addWidget(Game.Slide3label1)
Game.Slide3label1.setVisible(False)
layout.addWidget(Game.Slide3label2)
Game.Slide3label2.setVisible(False)
layout.addWidget(Game.Slide3label3)
Game.Slide3label3.setVisible(False)
layout.addWidget(Game.Slide3label4)
Game.Slide3label4.setVisible(False)
layout.addWidget(Game.Slide3label5)
Game.Slide3label5.setVisible(False)
layout.addWidget(Game.Slide3label6)
Game.Slide3label6.setVisible(False)
layout.addWidget(Game.Slide3label7)
Game.Slide3label7.setVisible(False)


#Slide3 Buttons
Game.Slide3Button1 = QPushButton("Grapple the skeleton.")
Game.Slide3Button2 = QPushButton("Slash the skeleton with your sword.")
Game.Slide3Button3 = QPushButton("Scare the skeleton off with your torchlight.")
Game.Slide3Button4 = QPushButton("Continue.")
layout.addWidget(Game.Slide3Button1)
layout.addWidget(Game.Slide3Button2)
layout.addWidget(Game.Slide3Button3)
layout.addWidget(Game.Slide3Button4)
Game.Slide3Button1.setVisible(False)
Game.Slide3Button2.setVisible(False)
Game.Slide3Button3.setVisible(False)
Game.Slide3Button4.setVisible(False)

#Slide4-------------------------------------------------------------
#Slide4 Image
Slide4Image = QPixmap("GameSatyr.png")
Game.Slide4ImageLabel = QLabel(Game)
Game.Slide4ImageLabel.setPixmap(Slide4Image)
layout.addWidget(Game.Slide4ImageLabel)
Game.Slide4ImageLabel.setVisible(False)

#Slide4 Text lines
Game.Slide4label1 = QLabel("You walk down the mossy path.")
Game.Slide4label2 = QLabel("The soft playing of a flute fills your ears as you come to an opening.")
Game.Slide4label3 = QLabel("You're met with a Satyr who asks you a riddle.")
Game.Slide4label4 = QLabel("'You cannot keep me until you have given me, what am I?'")
Game.Slide4label5 = QLabel("'Well done. Take this gold piece, may it serve you well.' +GAINED GOLD")
Game.Slide4label6 = QLabel("'Nah thats not it, move along.'")
layout.addWidget(Game.Slide4label1)
Game.Slide4label1.setVisible(False)
layout.addWidget(Game.Slide4label2)
Game.Slide4label2.setVisible(False)
layout.addWidget(Game.Slide4label3)
Game.Slide4label3.setVisible(False)
layout.addWidget(Game.Slide4label4)
Game.Slide4label4.setVisible(False)
layout.addWidget(Game.Slide4label5)
Game.Slide4label5.setVisible(False)
layout.addWidget(Game.Slide4label6)
Game.Slide4label6.setVisible(False)


#Slide4 Buttons
Game.Slide4Button1 = QPushButton("A gift")
Game.Slide4Button2 = QPushButton("A kiss")
Game.Slide4Button3 = QPushButton("A promise")
Game.Slide4Button4 = QPushButton("Continue.")
layout.addWidget(Game.Slide4Button1)
layout.addWidget(Game.Slide4Button2)
layout.addWidget(Game.Slide4Button3)
layout.addWidget(Game.Slide4Button4)
Game.Slide4Button1.setVisible(False)
Game.Slide4Button2.setVisible(False)
Game.Slide4Button3.setVisible(False)
Game.Slide4Button4.setVisible(False)

#Slide5-------------------------------------------------------------
#Slide5 Image
Slide5Image = QPixmap("GameSnake.png")
Game.Slide5ImageLabel = QLabel(Game)
Game.Slide5ImageLabel.setPixmap(Slide5Image)
layout.addWidget(Game.Slide5ImageLabel)
Game.Slide5ImageLabel.setVisible(False)

#Slide5 Text lines
Game.Slide5label1 = QLabel("You continue through the corridor and find an opening with pit of sand.")
Game.Slide5label2 = QLabel("The sand shifts and stirs and from out of it sprouts a large serpent.")
Game.Slide5label3 = QLabel("It bares its fangs at you and asks you a question.")
Game.Slide5label4 = QLabel("'Why have you come to thissss place tresssspasssser?'")
Game.Slide5label5 = QLabel("'Wrong, you have come to die!'")
Game.Slide5label6 = QLabel("The serpent sinks its fangs into you, killing you. You lose.")
Game.Slide5label7 = QLabel("'Good, kill that dragon for me. Take this key.'")
Game.Slide5label8 = QLabel("The snake allows you to pass. +GAINED KEY")
layout.addWidget(Game.Slide5label1)
Game.Slide5label1.setVisible(False)
layout.addWidget(Game.Slide5label2)
Game.Slide5label2.setVisible(False)
layout.addWidget(Game.Slide5label3)
Game.Slide5label3.setVisible(False)
layout.addWidget(Game.Slide5label4)
Game.Slide5label4.setVisible(False)
layout.addWidget(Game.Slide5label5)
Game.Slide5label5.setVisible(False)
layout.addWidget(Game.Slide5label6)
Game.Slide5label6.setVisible(False)
layout.addWidget(Game.Slide5label7)
Game.Slide5label7.setVisible(False)
layout.addWidget(Game.Slide5label8)
Game.Slide5label8.setVisible(False)


#Slide5 Buttons
Game.Slide5Button1 = QPushButton("To claim the treasure!")
Game.Slide5Button2 = QPushButton("To slay you!")
Game.Slide5Button3 = QPushButton("For glory!")
Game.Slide5Button4 = QPushButton("Continue.")
layout.addWidget(Game.Slide5Button1)
layout.addWidget(Game.Slide5Button2)
layout.addWidget(Game.Slide5Button3)
layout.addWidget(Game.Slide5Button4)
Game.Slide5Button1.setVisible(False)
Game.Slide5Button2.setVisible(False)
Game.Slide5Button3.setVisible(False)
Game.Slide5Button4.setVisible(False)

#Slide6-------------------------------------------------------------
#Slide6 Image
Slide6Image = QPixmap("Pitfall.png")
Game.Slide6ImageLabel = QLabel(Game)
Game.Slide6ImageLabel.setPixmap(Slide6Image)
layout.addWidget(Game.Slide6ImageLabel)
Game.Slide6ImageLabel.setVisible(False)

#Slide6 Text lines
Game.Slide6label1 = QLabel("You continue into a tight corridor, you sense something is wrong.")
Game.Slide6label2 = QLabel("A trap lays somewhere in this room.")
Game.Slide6label3 = QLabel("However, you know not what kind of trap.")
Game.Slide6label4 = QLabel("What will you do to avoid it?")
layout.addWidget(Game.Slide6label1)
Game.Slide6label1.setVisible(False)
layout.addWidget(Game.Slide6label2)
Game.Slide6label2.setVisible(False)
layout.addWidget(Game.Slide6label3)
Game.Slide6label3.setVisible(False)
layout.addWidget(Game.Slide6label4)
Game.Slide6label4.setVisible(False)



#Slide6 Buttons
Game.Slide6Button1 = QPushButton("Cling to the ceiling.")
Game.Slide6Button2 = QPushButton("Skirt the edge of the room.")
Game.Slide6Button3 = QPushButton("Just walk forward carefully.")
layout.addWidget(Game.Slide6Button1)
layout.addWidget(Game.Slide6Button2)
layout.addWidget(Game.Slide6Button3)
Game.Slide6Button1.setVisible(False)
Game.Slide6Button2.setVisible(False)
Game.Slide6Button3.setVisible(False)

#Slide7-------------------------------------------------------------
#Slide7 Image
Slide7Image = QPixmap("GameDog.png")
Game.Slide7ImageLabel = QLabel(Game)
Game.Slide7ImageLabel.setPixmap(Slide7Image)
layout.addWidget(Game.Slide7ImageLabel)
Game.Slide7ImageLabel.setVisible(False)

#Slide7 Text lines
Game.Slide7label1 = QLabel("You step into a clearing guarded by a large black dog.")
Game.Slide7label2 = QLabel("It snarls at you and lumbers over.")
Game.Slide7label3 = QLabel("What will you do?")
Game.Slide7label4 = QLabel("It doesn't work, the dog bites you killing you. You lose. Perhaps you were not prepared for this fight.")
Game.Slide7label5 = QLabel("You throw the BONE and the dog chases after it.")
Game.Slide7label6 = QLabel("The GHOSTBLADE glistens and in one slash you slice the dog in two.")
layout.addWidget(Game.Slide7label1)
Game.Slide7label1.setVisible(False)
layout.addWidget(Game.Slide7label2)
Game.Slide7label2.setVisible(False)
layout.addWidget(Game.Slide7label3)
Game.Slide7label3.setVisible(False)
layout.addWidget(Game.Slide7label4)
Game.Slide7label4.setVisible(False)
layout.addWidget(Game.Slide7label5)
Game.Slide7label5.setVisible(False)
layout.addWidget(Game.Slide7label6)
Game.Slide7label6.setVisible(False)



#Slide7 Buttons
Game.Slide7Button1 = QPushButton("Run.")
Game.Slide7Button2 = QPushButton("Attack")
Game.Slide7Button3 = QPushButton("Play fetch with the BONE. (USES BONE)")
Game.Slide7Button4 = QPushButton("Slash him with your GHOSTBLADE. (GHOSTBLADE)")
Game.Slide7Button5 = QPushButton("Continue.")
layout.addWidget(Game.Slide7Button1)
layout.addWidget(Game.Slide7Button2)
layout.addWidget(Game.Slide7Button3)
layout.addWidget(Game.Slide7Button4)
layout.addWidget(Game.Slide7Button5)
Game.Slide7Button1.setVisible(False)
Game.Slide7Button2.setVisible(False)
Game.Slide7Button3.setVisible(False)
Game.Slide7Button4.setVisible(False)
Game.Slide7Button5.setVisible(False)

#Slide8-------------------------------------------------------------
#Slide8 Image
Slide8Image = QPixmap("GameGhost.png")
Game.Slide8ImageLabel = QLabel(Game)
Game.Slide8ImageLabel.setPixmap(Slide8Image)
layout.addWidget(Game.Slide8ImageLabel)
Game.Slide8ImageLabel.setVisible(False)

#Slide8 Text lines
Game.Slide8label1 = QLabel("You fall into a pit trap and you're shrouded in darkness.")
Game.Slide8label2 = QLabel("An ethereal light glows before you, a ghost approaches.")
Game.Slide8label3 = QLabel("What will you do?")
Game.Slide8label4 = QLabel("Its useless, you feel cold as the ghost saps the life out of your body. You lose.")
Game.Slide8label5 = QLabel("Your prayer is heard, the ghost retreats, leaving behind a glistening blade. +GAINED GHOSTBLADE")  
layout.addWidget(Game.Slide8label1)
Game.Slide8label1.setVisible(False)
layout.addWidget(Game.Slide8label2)
Game.Slide8label2.setVisible(False)
layout.addWidget(Game.Slide8label3)
Game.Slide8label3.setVisible(False)
layout.addWidget(Game.Slide8label4)
Game.Slide8label4.setVisible(False)
layout.addWidget(Game.Slide8label5)
Game.Slide8label5.setVisible(False)



#Slide8 Buttons
Game.Slide8Button1 = QPushButton("Run.")
Game.Slide8Button2 = QPushButton("Attack.")
Game.Slide8Button3 = QPushButton("Pray.")
Game.Slide8Button4 = QPushButton("Continue.")
layout.addWidget(Game.Slide8Button1)
layout.addWidget(Game.Slide8Button2)
layout.addWidget(Game.Slide8Button3)
layout.addWidget(Game.Slide8Button4)
Game.Slide8Button1.setVisible(False)
Game.Slide8Button2.setVisible(False)
Game.Slide8Button3.setVisible(False)
Game.Slide8Button4.setVisible(False)

#Slide9-------------------------------------------------------------
#Slide9 Image
Slide9Image = QPixmap("GameGoblinDoor.png")
Game.Slide9ImageLabel = QLabel(Game)
Game.Slide9ImageLabel.setPixmap(Slide9Image)
layout.addWidget(Game.Slide9ImageLabel)
Game.Slide9ImageLabel.setVisible(False)

#Slide9 Text lines
Game.Slide9label1 = QLabel("In front of you is a towering red door.")
Game.Slide9label2 = QLabel("You're certain that the treasure is behind it.")
Game.Slide9label3 = QLabel("In front of the door stands a small goblin.")
Game.Slide9label4 = QLabel("He says, 'You'll need a key if you wish to get in there, I can sell one to you for GOLD.'")
Game.Slide9label5 = QLabel("'A pleasure to do business with you!' +GAINED KEY")
Game.Slide9label6 = QLabel("The goblin is too quick and scurries off. You now have no chance of getting in the door. You lose.")
Game.Slide9label7 = QLabel("Your GHOSTBLADE glistens as you slice the goblin in two, taking the key. +GAINED KEY")
Game.Slide9label8 = QLabel("'Well carry on then.' says the goblin.")
Game.Slide9label9 = QLabel("You slot the key into the door and push it open.")
layout.addWidget(Game.Slide9label1)
Game.Slide9label1.setVisible(False)
layout.addWidget(Game.Slide9label2)
Game.Slide9label2.setVisible(False)
layout.addWidget(Game.Slide9label3)
Game.Slide9label3.setVisible(False)
layout.addWidget(Game.Slide9label4)
Game.Slide9label4.setVisible(False)
layout.addWidget(Game.Slide9label5)
Game.Slide9label5.setVisible(False)
layout.addWidget(Game.Slide9label6)
Game.Slide9label6.setVisible(False)
layout.addWidget(Game.Slide9label7)
Game.Slide9label7.setVisible(False)
layout.addWidget(Game.Slide9label8)
Game.Slide9label8.setVisible(False)
layout.addWidget(Game.Slide9label9)
Game.Slide9label9.setVisible(False)



#Slide9 Buttons
Game.Slide9Button1 = QPushButton("Attempt to steal the key.")
Game.Slide9Button2 = QPushButton("I already have a key. (USES KEY)")
Game.Slide9Button3 = QPushButton("Slash at him with your GHOSTBLADE. (GHOSTBLADE)")
Game.Slide9Button4 = QPushButton("Buy the key. (USES GOLD)")
Game.Slide9Button5 = QPushButton("Continue.")
layout.addWidget(Game.Slide9Button1)
layout.addWidget(Game.Slide9Button2)
layout.addWidget(Game.Slide9Button3)
layout.addWidget(Game.Slide9Button4)
layout.addWidget(Game.Slide9Button5)
Game.Slide9Button1.setVisible(False)
Game.Slide9Button2.setVisible(False)
Game.Slide9Button3.setVisible(False)
Game.Slide9Button4.setVisible(False)
Game.Slide9Button5.setVisible(False)

#Slide10-------------------------------------------------------------
#Slide10 Image
Slide10Image = QPixmap("GameDragon.png")
Game.Slide10ImageLabel = QLabel(Game)
Game.Slide10ImageLabel.setPixmap(Slide10Image)
layout.addWidget(Game.Slide10ImageLabel)
Game.Slide10ImageLabel.setVisible(False)

#Slide10 Text lines
Game.Slide10label1 = QLabel("Before you lies the treasure you seek.")
Game.Slide10label2 = QLabel("On top of it sits a large, firebreathing dragon.")
Game.Slide10label3 = QLabel("'THIS TREASURE IS MINE, DIE INTRUDER!' says the dragon.")
Game.Slide10label4 = QLabel("What will you do?")
Game.Slide10label5 = QLabel("Fire sprouts from the dragons throat and you are covered in flame. You lose.")
Game.Slide10label6 = QLabel("In one swing your GHOSTBLADE cuts straight through the dragons neck, severing it. The beast is slain.")
Game.Slide10label7 = QLabel("You claim the treasure for your own, ending your journey. The end.")
Game.Slide10label8 = QLabel("'Aww, how sweet of you. I take it back, you may leave.' says the dragon")
Game.Slide10label9 = QLabel("You walk out of the cave realizing the treasure isn't worth it. The end.")
layout.addWidget(Game.Slide10label1)
Game.Slide10label1.setVisible(False)
layout.addWidget(Game.Slide10label2)
Game.Slide10label2.setVisible(False)
layout.addWidget(Game.Slide10label3)
Game.Slide10label3.setVisible(False)
layout.addWidget(Game.Slide10label4)
Game.Slide10label4.setVisible(False)
layout.addWidget(Game.Slide10label5)
Game.Slide10label5.setVisible(False)
layout.addWidget(Game.Slide10label6)
Game.Slide10label6.setVisible(False)
layout.addWidget(Game.Slide10label7)
Game.Slide10label7.setVisible(False)
layout.addWidget(Game.Slide10label8)
Game.Slide10label8.setVisible(False)
layout.addWidget(Game.Slide10label9)
Game.Slide10label9.setVisible(False)



#Slide10 Buttons
Game.Slide10Button1 = QPushButton("Grab as much treasure as you can and bolt.")
Game.Slide10Button2 = QPushButton("Attack the dragon with your sword.")
Game.Slide10Button3 = QPushButton("Attack the dragon with your GHOSTBLADE. (GHOSTBLADE)")
Game.Slide10Button4 = QPushButton("Offer the dragon your GOLD for his mercy. (USES GOLD)")
layout.addWidget(Game.Slide10Button1)
layout.addWidget(Game.Slide10Button2)
layout.addWidget(Game.Slide10Button3)
layout.addWidget(Game.Slide10Button4)
Game.Slide10Button1.setVisible(False)
Game.Slide10Button2.setVisible(False)
Game.Slide10Button3.setVisible(False)
Game.Slide10Button4.setVisible(False)


#BUTTONSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs
Game.RestartButton = QPushButton("Restart?")
layout.addWidget(Game.RestartButton)
Game.RestartButton.setVisible(False)

Game.RestartButton.clicked.connect(Restart)

Game.Slide1Button1.clicked.connect(Slide2SetVis)

Game.Slide2Button1.clicked.connect(Slide3SetVis)
Game.Slide2Button2.clicked.connect(Slide4SetVis)

Game.Slide3Button1.clicked.connect(Slide3p1SetVis)
Game.Slide3Button2.clicked.connect(Slide3p2SetVis)
Game.Slide3Button3.clicked.connect(Slide3p3SetVis)
Game.Slide3Button4.clicked.connect(Slide5SetVis)

Game.Slide4Button1.clicked.connect(Slide4p2SetVis)
Game.Slide4Button2.clicked.connect(Slide4p2SetVis)
Game.Slide4Button3.clicked.connect(Slide4p1SetVis)
Game.Slide4Button4.clicked.connect(Slide6SetVis)

Game.Slide5Button1.clicked.connect(Slide5p2SetVis)
Game.Slide5Button2.clicked.connect(Slide5p1SetVis)
Game.Slide5Button3.clicked.connect(Slide5p2SetVis)
Game.Slide5Button4.clicked.connect(Slide7SetVis)

Game.Slide6Button1.clicked.connect(Slide7SetVis)
Game.Slide6Button2.clicked.connect(Slide7SetVis)
Game.Slide6Button3.clicked.connect(Slide8SetVis)

Game.Slide7Button1.clicked.connect(Slide7p1SetVis)
Game.Slide7Button2.clicked.connect(Slide7p1SetVis)
Game.Slide7Button3.clicked.connect(Slide7p2SetVis)
Game.Slide7Button4.clicked.connect(Slide7p3SetVis)
Game.Slide7Button5.clicked.connect(Slide9SetVis)

Game.Slide8Button1.clicked.connect(Slide8p1SetVis)
Game.Slide8Button2.clicked.connect(Slide8p1SetVis)
Game.Slide8Button3.clicked.connect(Slide8p2SetVis)
Game.Slide8Button4.clicked.connect(Slide7SetVis)

Game.Slide9Button1.clicked.connect(Slide9p1SetVis)
Game.Slide9Button2.clicked.connect(Slide9p2SetVis)
Game.Slide9Button3.clicked.connect(Slide9p3SetVis)
Game.Slide9Button4.clicked.connect(Slide9p4SetVis)
Game.Slide9Button5.clicked.connect(Slide10SetVis)

Game.Slide10Button1.clicked.connect(Slide10p1SetVis)
Game.Slide10Button2.clicked.connect(Slide10p1SetVis)
Game.Slide10Button3.clicked.connect(Slide10p2SetVis)
Game.Slide10Button4.clicked.connect(Slide10p3SetVis)







#Show window and exit system when closed.
Game.show() 
sys.exit(app.exec())


playerHealth = 100






