#############################################################
# Setup and import all modules
#############################################################

# Import access to command line arguments
import sys

# Import PyQt5 QtCore modules
from PyQt5.QtCore import (
	QSize,
	Qt
)

# Import PyQt5 widgets
from PyQt5.QtWidgets import (
	QApplication,
	QCheckBox,
	QComboBox,
	QDateEdit,
	QDateTimeEdit,
	QDial,
	QDoubleSpinBox,
	QFontComboBox,
	QLabel,
	QLCDNumber,
	QLineEdit,
	QMainWindow,
	QProgressBar,
	QPushButton,
	QRadioButton,
	QSlider,
	QSpinBox,
	QTimeEdit,
	QVBoxLayout,
	QHBoxLayout,
	QGridLayout,
	QStackedLayout,
	QWidget
)

# Import PyQt5 QtGui modules
from PyQt5.QtGui import (
	QPalette,
	QColor
)

# Create instance of a PyQt5 application
app = QApplication(sys.argv)


#############################################################
# Class for Main Window
#############################################################

class MainWindow(QWidget):

	#########################################################
	# Function for creating a generic button
	#########################################################

	def createButton(self, text, fontSize, x, y, width, height, cornerRadius, redVal, greenVal, blueVal, function):
		
		# Sets values for button press
		if redVal < 230:
			redVal2 = redVal + 25
		else:
			redVal2 = 255

		if greenVal < 230:
			greenVal2 = greenVal + 25
		else:
			greenVal2 = 255

		if blueVal < 230:
			blueVal2 = blueVal + 25
		else:
			blueVal2 = 255

		if fontSize > 1:
			fontSize2 = fontSize - 1
		else:
			fontSize2 = 1
		
		# Set button parameters
		button = QPushButton(self)
		button.setText(text)
		button.move(x, y)
		button.setFixedSize(width, height)
		button.setStyleSheet(
			"""
			QPushButton
			{
			background:rgb(""" + str(redVal) + """, """ + str(greenVal) + """, """ + str(blueVal) + """);
			font-size:""" + str(fontSize) + """px;
			color:rgb(65, 65, 65);
			font:bold; 
			border-radius:""" + str(cornerRadius) + """px;
			border : 3px solid rgb(65, 65, 65);
			}

			QPushButton::pressed
			{
			background:rgb(""" + str(redVal2) + """, """ + str(greenVal2) + """, """ + str(blueVal2) + """);
			font-size:""" + str(fontSize2) + """px;
			color:rgb(95, 95, 95);
			font:bold;
			border-radius:""" + str(cornerRadius) + """px;
			border : 3px solid rgb(95, 95, 95);
			}
			"""
			)

		# Set button functions
		button.setCheckable(True)
		button.clicked.connect(function)

		# Return button
		return button


	#########################################################
	# Function for creating Main Window
	#########################################################

	def __init__(self, windowTitle, width, height, frame):
		super().__init__()
		
		self.setWindowTitle(windowTitle)			# Set title of window
		self.setFixedSize(QSize(width, height))		# Set window size
		
		# Turns OFF standard window frame if specified
		if frame == False:
			self.setWindowFlag(Qt.FramelessWindowHint)


		#####################################################
		# Create all buttons in Main Window
		#####################################################

		self.button1 = self.createButton("button 1", 36, 275, 80, 200, 200, 20, 255, 109, 126, self.button1Selected)
		self.button2 = self.createButton("button 2", 36, 550, 80, 200, 200, 20, 245, 255, 164, self.button2Selected)
		self.button3 = self.createButton("button 3", 36, 275, 340, 200, 200, 20, 176, 255, 213, self.button3Selected)
		self.button4 = self.createButton("button 4", 36, 550, 340, 200, 200, 20, 173, 179, 255, self.button4Selected)
		self.exitButton = self.createButton("X", 28, 964, 1, 60, 60, 5, 255, 100, 100, self.exitSelected)


	#########################################################
	# Interrupt routines for all button presses
	#########################################################

	def button1Selected(self, checked):
		print("button 1", checked)

	def button2Selected(self, checked):
		print("button 2", checked)

	def button3Selected(self, checked):
		print("button 3", checked)

	def button4Selected(self, checked):
		print("button 4", checked)

	def exitSelected(self, checked):
		print("Program Quit")
		QApplication.quit()


#############################################################
# Create Main Window
#############################################################

mainWindow = MainWindow("Main Window", 1024, 648, False)	# Create instance of applications main window (1024, 648)
mainWindow.show()											# Display main window (hidden by default)

#############################################################
# Create event loop
#############################################################

app.exec_()