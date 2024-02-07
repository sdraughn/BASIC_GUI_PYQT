#############################################################
# Setup and import all modules
#############################################################

# Import access to command line arguments
import sys

# Import PyQt5 QtCore modules
from PyQt5.QtCore import (
	Qt,
	QSize,
	QRectF
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
	QGraphicsRectItem,
	QStackedWidget,
	QWidget
)

# Import PyQt5 QtGui modules
from PyQt5.QtGui import (
	QPalette,
	QColor,
	QPainter,
	QPainterPath,
	QBrush,
	QPen,
	QFont,
	QPixmap
)

# Create instance of a PyQt5 application
app = QApplication(sys.argv)

#############################################################
# Window 1
#############################################################

class Window1GUI(QWidget):

	#########################################################
	# Function for creating a generic button
	#########################################################

	def createButton(self, text, fontSize, x, y, width, height, border, cornerRadius, redVal, greenVal, blueVal, function):
		
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
			border : """ + str(border) + """px solid rgb(65, 65, 65);
			}

			QPushButton::pressed
			{
			background:rgb(""" + str(redVal2) + """, """ + str(greenVal2) + """, """ + str(blueVal2) + """);
			font-size:""" + str(fontSize2) + """px;
			color:rgb(95, 95, 95);
			font:bold;
			border-radius:""" + str(cornerRadius + 4) + """px;
			border : """ + str(border) + """px solid rgb(95, 95, 95);
			}
			"""
			)

		# Set button functions
		button.setCheckable(True)
		button.clicked.connect(function)

		return button
	
	#########################################################
	# Function for creating an image on Window 1
	#########################################################

	def createImage(self, image, x, y, xScale, yScale):

		pixmap = QPixmap(image)
		pixmap = pixmap.scaled(xScale, yScale)

		label = QLabel(self)
		label.setStyleSheet("border: 2px solid black;")
		label.setPixmap(pixmap)
		label.move(x, y)

		return label

	#########################################################
	# Function for creating Window 1
	#########################################################

	def __init__(self, windowTitle, width, height, redVal, greenVal, blueVal, frame):

		super().__init__()
		
		self.setWindowTitle(windowTitle)			# Set title of window
		self.setFixedSize(QSize(width, height))		# Set window size
		self.setStyleSheet("""QWidget{background:rgb(""" + str(redVal) + """, """ + str(greenVal) + """, """ + str(blueVal) + """);}""")
		
		# Turns OFF standard window frame if specified
		if frame == False:
			self.setWindowFlag(Qt.FramelessWindowHint)

		#####################################################
		# Create and add all items in Window 1
		#####################################################

		# Create and place main buttons
		self.button1 = self.createButton("Button \n 1", 36, 315, 140, 200, 160, 3, 10, 250, 152, 164, self.button1Selected)
		self.button2 = self.createButton("Button \n 2", 36, 580, 140, 200, 160, 3, 10, 249, 255, 199, self.button2Selected)
		self.button3 = self.createButton("Button \n 3", 36, 315, 360, 200, 160, 3, 10, 199, 255, 229, self.button3Selected)
		self.button4 = self.createButton("Button \n 4", 36, 580, 360, 200, 160, 3, 10, 206, 199, 255, self.button4Selected)

		# Create and place all sidebar window select buttons
		self.window1Button = self.createButton("W1", 28, 0, 160, 80, 80, 1, 0, 235, 204, 204, self.window1ButtonSelected)
		self.window2Button = self.createButton("W2", 28, 0, 240, 80, 80, 1, 0, 235, 226, 204, self.window2ButtonSelected)
		self.window3Button = self.createButton("W3", 28, 0, 320, 80, 80, 1, 0, 204, 235, 223, self.window3ButtonSelected)
		self.window4Button = self.createButton("W4", 28, 0, 400, 80, 80, 1, 0, 204, 204, 235, self.window4ButtonSelected)

		# Create and place exit application button
		self.exitButton = self.createButton("X", 28, 964, 1, 60, 60, 3, 0, 255, 100, 100, self.exitSelected)

		# Create and place Bravo logo
		self.image = self.createImage('Bravo_Logo_ONLY.png', 0, 0, 77, 77)

		return
	
	#########################################################
	# Draw all shapes, lines and text for Window 1
	#########################################################

	def paintEvent(self, event):

		# Draw topbar rectangles
		topBar = QPainter(self)
		topBar.setPen(QColor(0, 0, 0))
		topBar.drawRect(0, 0, 1024, 60)
		topBar.setBrush(QColor(144, 144, 145))
		topBar.drawRect(0, 0, 1024, 60)

		# Draw sidebar rectangles
		sideBar = QPainter(self)
		sideBar.setPen(QColor(0, 0, 0))
		sideBar.drawRect(0, 0, 80, 607)
		sideBar.setBrush(QColor(144, 144, 145))
		sideBar.drawRect(0, 0, 80, 606)

		# Draw Window 1 header text
		headerText = QPainter(self)
		headerText.setPen(QColor(35, 35, 35))
		headerText.setFont(QFont('Arial', 24, 63))
		headerText.drawText(90, 48, "Window 1")

	#########################################################
	# Interrupt routines for all Window 1 button presses
	#########################################################

	def button1Selected(self, checked):
		print("Button 1", checked)

	def button2Selected(self, checked):
		print("Button 2", checked)

	def button3Selected(self, checked):
		print("Button 3", checked)

	def button4Selected(self, checked):
		print("Button 4", checked)

	def window1ButtonSelected(self, checked):
		print("Switched to Window 1", checked)
		stackedWidget.setCurrentWidget(window1)

	def window2ButtonSelected(self, checked):
		print("Switched to Window 2", checked)
		stackedWidget.setCurrentWidget(window2)

	def window3ButtonSelected(self, checked):
		print("Switched to Window 3", checked)
		stackedWidget.setCurrentWidget(window3)

	def window4ButtonSelected(self, checked):
		print("Switched to Window 4", checked)
		stackedWidget.setCurrentWidget(window4)

	def exitSelected(self, checked):
		print("Program Quit")
		QApplication.quit()

#############################################################
# Window 2
#############################################################

class Window2GUI(QWidget):

	#########################################################
	# Function for creating a generic button
	#########################################################

	def createButton(self, text, fontSize, x, y, width, height, border, cornerRadius, redVal, greenVal, blueVal, function):
		
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
			border : """ + str(border) + """px solid rgb(65, 65, 65);
			}

			QPushButton::pressed
			{
			background:rgb(""" + str(redVal2) + """, """ + str(greenVal2) + """, """ + str(blueVal2) + """);
			font-size:""" + str(fontSize2) + """px;
			color:rgb(95, 95, 95);
			font:bold;
			border-radius:""" + str(cornerRadius + 4) + """px;
			border : """ + str(border) + """px solid rgb(95, 95, 95);
			}
			"""
			)

		# Set button functions
		button.setCheckable(True)
		button.clicked.connect(function)

		# Return button
		return button
	
	#########################################################
	# Function for creating an image on Window 2
	#########################################################

	def createImage(self, image, x, y, xScale, yScale):

		pixmap = QPixmap(image)
		pixmap = pixmap.scaled(xScale, yScale)

		label = QLabel(self)
		label.setStyleSheet("border: 2px solid black;")
		label.setPixmap(pixmap)
		label.move(x, y)

		return label

	#########################################################
	# Function for creating Window 2
	#########################################################

	def __init__(self, windowTitle, width, height, redVal, greenVal, blueVal, frame):

		super().__init__()
		
		self.setWindowTitle(windowTitle)			# Set title of window
		self.setFixedSize(QSize(width, height))		# Set window size
		self.setStyleSheet("""QWidget{background:rgb(""" + str(redVal) + """, """ + str(greenVal) + """, """ + str(blueVal) + """);}""")
		
		# Turns OFF standard window frame if specified
		if frame == False:
			self.setWindowFlag(Qt.FramelessWindowHint)

		#####################################################
		# Create and add all items in Window 2
		#####################################################

		# Create and place main buttons
		self.button1 = self.createButton("Button \n 5", 36, 315, 140, 200, 160, 3, 10, 250, 152, 164, self.button1Selected)
		self.button2 = self.createButton("Button \n 6", 36, 580, 140, 200, 160, 3, 10, 249, 255, 199, self.button2Selected)
		self.button3 = self.createButton("Button \n 7", 36, 315, 360, 200, 160, 3, 10, 199, 255, 229, self.button3Selected)
		self.button4 = self.createButton("Button \n 8", 36, 580, 360, 200, 160, 3, 10, 206, 199, 255, self.button4Selected)

		# Create and place all sidebar window select buttons
		self.window1Button = self.createButton("W1", 28, 0, 160, 80, 80, 1, 0, 235, 204, 204, self.window1ButtonSelected)
		self.window2Button = self.createButton("W2", 28, 0, 240, 80, 80, 1, 0, 235, 226, 204, self.window2ButtonSelected)
		self.window3Button = self.createButton("W3", 28, 0, 320, 80, 80, 1, 0, 204, 235, 223, self.window3ButtonSelected)
		self.window4Button = self.createButton("W4", 28, 0, 400, 80, 80, 1, 0, 204, 204, 235, self.window4ButtonSelected)

		# Create and place exit application button
		self.exitButton = self.createButton("X", 28, 964, 1, 60, 60, 3, 0, 255, 100, 100, self.exitSelected)

		# Create and place Bravo logo
		self.image = self.createImage('Bravo_Logo_ONLY.png', 0, 0, 77, 77)

		return
	
	#########################################################
	# Draw all shapes, lines and text for Window 2
	#########################################################

	def paintEvent(self, event):

		# Draw topbar rectangles
		topBar = QPainter(self)
		topBar.setPen(QColor(0, 0, 0))
		topBar.drawRect(0, 0, 1024, 60)
		topBar.setBrush(QColor(144, 144, 145))
		topBar.drawRect(0, 0, 1024, 60)

		# Draw sidebar rectangles
		sideBar = QPainter(self)
		sideBar.setPen(QColor(0, 0, 0))
		sideBar.drawRect(0, 0, 80, 607)
		sideBar.setBrush(QColor(144, 144, 145))
		sideBar.drawRect(0, 0, 80, 606)

		# Draw Window 1 header text
		headerText = QPainter(self)
		headerText.setPen(QColor(35, 35, 35))
		headerText.setFont(QFont('Arial', 24, 63))
		headerText.drawText(90, 48, "Window 2")

	#########################################################
	# Interrupt routines for all Window 2 button presses
	#########################################################

	def button1Selected(self, checked):
		print("Button 5", checked)

	def button2Selected(self, checked):
		print("Button 6", checked)

	def button3Selected(self, checked):
		print("Button 7", checked)

	def button4Selected(self, checked):
		print("Button 8", checked)

	def window1ButtonSelected(self, checked):
		print("Switched to Window 1", checked)
		stackedWidget.setCurrentWidget(window1)

	def window2ButtonSelected(self, checked):
		print("Switched to Window 2", checked)
		stackedWidget.setCurrentWidget(window2)

	def window3ButtonSelected(self, checked):
		print("Switched to Window 3", checked)
		stackedWidget.setCurrentWidget(window3)

	def window4ButtonSelected(self, checked):
		print("Switched to Window 4", checked)
		stackedWidget.setCurrentWidget(window4)

	def exitSelected(self, checked):
		print("Program Quit")
		QApplication.quit()

#############################################################
# Window 3
#############################################################

class Window3GUI(QWidget):

	#########################################################
	# Function for creating a generic button
	#########################################################

	def createButton(self, text, fontSize, x, y, width, height, border, cornerRadius, redVal, greenVal, blueVal, function):
		
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
			border : """ + str(border) + """px solid rgb(65, 65, 65);
			}

			QPushButton::pressed
			{
			background:rgb(""" + str(redVal2) + """, """ + str(greenVal2) + """, """ + str(blueVal2) + """);
			font-size:""" + str(fontSize2) + """px;
			color:rgb(95, 95, 95);
			font:bold;
			border-radius:""" + str(cornerRadius + 4) + """px;
			border : """ + str(border) + """px solid rgb(95, 95, 95);
			}
			"""
			)

		# Set button functions
		button.setCheckable(True)
		button.clicked.connect(function)

		# Return button
		return button
	
	#########################################################
	# Function for creating an image on Window 3
	#########################################################

	def createImage(self, image, x, y, xScale, yScale):

		pixmap = QPixmap(image)
		pixmap = pixmap.scaled(xScale, yScale)

		label = QLabel(self)
		label.setStyleSheet("border: 2px solid black;")
		label.setPixmap(pixmap)
		label.move(x, y)

		return label

	#########################################################
	# Function for creating Window 3
	#########################################################

	def __init__(self, windowTitle, width, height, redVal, greenVal, blueVal, frame):

		super().__init__()
		
		self.setWindowTitle(windowTitle)			# Set title of window
		self.setFixedSize(QSize(width, height))		# Set window size
		self.setStyleSheet("""QWidget{background:rgb(""" + str(redVal) + """, """ + str(greenVal) + """, """ + str(blueVal) + """);}""")
		
		# Turns OFF standard window frame if specified
		if frame == False:
			self.setWindowFlag(Qt.FramelessWindowHint)

		#####################################################
		# Create and add all items in Window 3
		#####################################################

		# Create and place main buttons
		self.button1 = self.createButton("Button \n 9", 36, 315, 140, 200, 160, 3, 10, 250, 152, 164, self.button1Selected)
		self.button2 = self.createButton("Button \n 10", 36, 580, 140, 200, 160, 3, 10, 249, 255, 199, self.button2Selected)
		self.button3 = self.createButton("Button \n 11", 36, 315, 360, 200, 160, 3, 10, 199, 255, 229, self.button3Selected)
		self.button4 = self.createButton("Button \n 12", 36, 580, 360, 200, 160, 3, 10, 206, 199, 255, self.button4Selected)

		# Create and place all sidebar window select buttons
		self.window1Button = self.createButton("W1", 28, 0, 160, 80, 80, 1, 0, 235, 204, 204, self.window1ButtonSelected)
		self.window2Button = self.createButton("W2", 28, 0, 240, 80, 80, 1, 0, 235, 226, 204, self.window2ButtonSelected)
		self.window3Button = self.createButton("W3", 28, 0, 320, 80, 80, 1, 0, 204, 235, 223, self.window3ButtonSelected)
		self.window4Button = self.createButton("W4", 28, 0, 400, 80, 80, 1, 0, 204, 204, 235, self.window4ButtonSelected)

		# Create and place exit application button
		self.exitButton = self.createButton("X", 28, 964, 1, 60, 60, 3, 0, 255, 100, 100, self.exitSelected)

		# Create and place Bravo logo
		self.image = self.createImage('Bravo_Logo_ONLY.png', 0, 0, 77, 77)

		return
	
	#########################################################
	# Draw all shapes, lines and text for Window 3
	#########################################################

	def paintEvent(self, event):

		# Draw topbar rectangles
		topBar = QPainter(self)
		topBar.setPen(QColor(0, 0, 0))
		topBar.drawRect(0, 0, 1024, 60)
		topBar.setBrush(QColor(144, 144, 145))
		topBar.drawRect(0, 0, 1024, 60)

		# Draw sidebar rectangles
		sideBar = QPainter(self)
		sideBar.setPen(QColor(0, 0, 0))
		sideBar.drawRect(0, 0, 80, 607)
		sideBar.setBrush(QColor(144, 144, 145))
		sideBar.drawRect(0, 0, 80, 606)

		# Draw Window 1 header text
		headerText = QPainter(self)
		headerText.setPen(QColor(35, 35, 35))
		headerText.setFont(QFont('Arial', 24, 63))
		headerText.drawText(90, 48, "Window 3")

	#########################################################
	# Interrupt routines for all Window 3 button presses
	#########################################################

	def button1Selected(self, checked):
		print("Button 9", checked)

	def button2Selected(self, checked):
		print("Button 10", checked)

	def button3Selected(self, checked):
		print("Button 11", checked)

	def button4Selected(self, checked):
		print("Button 12", checked)

	def window1ButtonSelected(self, checked):
		print("Switched to Window 1", checked)
		stackedWidget.setCurrentWidget(window1)

	def window2ButtonSelected(self, checked):
		print("Switched to Window 2", checked)
		stackedWidget.setCurrentWidget(window2)

	def window3ButtonSelected(self, checked):
		print("Switched to Window 3", checked)
		stackedWidget.setCurrentWidget(window3)

	def window4ButtonSelected(self, checked):
		print("Switched to Window 4", checked)
		stackedWidget.setCurrentWidget(window4)

	def exitSelected(self, checked):
		print("Program Quit")
		QApplication.quit()

#############################################################
# Window 4
#############################################################

class Window4GUI(QWidget):

	#########################################################
	# Function for creating a generic button
	#########################################################

	def createButton(self, text, fontSize, x, y, width, height, border, cornerRadius, redVal, greenVal, blueVal, function):
		
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
			border : """ + str(border) + """px solid rgb(65, 65, 65);
			}

			QPushButton::pressed
			{
			background:rgb(""" + str(redVal2) + """, """ + str(greenVal2) + """, """ + str(blueVal2) + """);
			font-size:""" + str(fontSize2) + """px;
			color:rgb(95, 95, 95);
			font:bold;
			border-radius:""" + str(cornerRadius + 4) + """px;
			border : """ + str(border) + """px solid rgb(95, 95, 95);
			}
			"""
			)

		# Set button functions
		button.setCheckable(True)
		button.clicked.connect(function)

		# Return button
		return button
	
	#########################################################
	# Function for creating an image on Window 4
	#########################################################

	def createImage(self, image, x, y, xScale, yScale):

		pixmap = QPixmap(image)
		pixmap = pixmap.scaled(xScale, yScale)

		label = QLabel(self)
		label.setStyleSheet("border: 2px solid black;")
		label.setPixmap(pixmap)
		label.move(x, y)

		return label

	#########################################################
	# Function for creating Window 4
	#########################################################

	def __init__(self, windowTitle, width, height, redVal, greenVal, blueVal, frame):

		super().__init__()
		
		self.setWindowTitle(windowTitle)			# Set title of window
		self.setFixedSize(QSize(width, height))		# Set window size
		self.setStyleSheet("""QWidget{background:rgb(""" + str(redVal) + """, """ + str(greenVal) + """, """ + str(blueVal) + """);}""")
		
		# Turns OFF standard window frame if specified
		if frame == False:
			self.setWindowFlag(Qt.FramelessWindowHint)

		#####################################################
		# Create and add all items in Window 4
		#####################################################

		# Create and place main buttons
		self.button1 = self.createButton("Button \n 13", 36, 315, 140, 200, 160, 3, 10, 250, 152, 164, self.button1Selected)
		self.button2 = self.createButton("Button \n 14", 36, 580, 140, 200, 160, 3, 10, 249, 255, 199, self.button2Selected)
		self.button3 = self.createButton("Button \n 15", 36, 315, 360, 200, 160, 3, 10, 199, 255, 229, self.button3Selected)
		self.button4 = self.createButton("Button \n 16", 36, 580, 360, 200, 160, 3, 10, 206, 199, 255, self.button4Selected)

		# Create and place all sidebar window select buttons
		self.window1Button = self.createButton("W1", 28, 0, 160, 80, 80, 1, 0, 235, 204, 204, self.window1ButtonSelected)
		self.window2Button = self.createButton("W2", 28, 0, 240, 80, 80, 1, 0, 235, 226, 204, self.window2ButtonSelected)
		self.window3Button = self.createButton("W3", 28, 0, 320, 80, 80, 1, 0, 204, 235, 223, self.window3ButtonSelected)
		self.window4Button = self.createButton("W4", 28, 0, 400, 80, 80, 1, 0, 204, 204, 235, self.window4ButtonSelected)

		# Create and place exit application button
		self.exitButton = self.createButton("X", 28, 964, 1, 60, 60, 3, 0, 255, 100, 100, self.exitSelected)

		# Create and place Bravo logo
		self.image = self.createImage('Bravo_Logo_ONLY.png', 0, 0, 77, 77)

		return
	
	#########################################################
	# Draw all shapes, lines and text for Window 4
	#########################################################

	def paintEvent(self, event):

		# Draw topbar rectangles
		topBar = QPainter(self)
		topBar.setPen(QColor(0, 0, 0))
		topBar.drawRect(0, 0, 1024, 60)
		topBar.setBrush(QColor(144, 144, 145))
		topBar.drawRect(0, 0, 1024, 60)

		# Draw sidebar rectangles
		sideBar = QPainter(self)
		sideBar.setPen(QColor(0, 0, 0))
		sideBar.drawRect(0, 0, 80, 607)
		sideBar.setBrush(QColor(144, 144, 145))
		sideBar.drawRect(0, 0, 80, 606)

		# Draw Window 1 header text
		headerText = QPainter(self)
		headerText.setPen(QColor(35, 35, 35))
		headerText.setFont(QFont('Arial', 24, 63))
		headerText.drawText(90, 48, "Window 4")

	#########################################################
	# Interrupt routines for all Window 4 button presses
	#########################################################

	def button1Selected(self, checked):
		print("Button 13", checked)

	def button2Selected(self, checked):
		print("Button 14", checked)

	def button3Selected(self, checked):
		print("Button 15", checked)

	def button4Selected(self, checked):
		print("Button 16", checked)

	def window1ButtonSelected(self, checked):
		print("Switched to Window 1", checked)
		stackedWidget.setCurrentWidget(window1)

	def window2ButtonSelected(self, checked):
		print("Switched to Window 2", checked)
		stackedWidget.setCurrentWidget(window2)

	def window3ButtonSelected(self, checked):
		print("Switched to Window 3", checked)
		stackedWidget.setCurrentWidget(window3)

	def window4ButtonSelected(self, checked):
		print("Switched to Window 4", checked)
		stackedWidget.setCurrentWidget(window4)

	def exitSelected(self, checked):
		print("Program Quit")
		QApplication.quit()

#############################################################
# Create all windows and stack them
#############################################################

window1 = Window1GUI("Window 1", 1024, 648, 235, 204, 204, False)	# Create instance of applications Window 1 (1024, 648)
window2 = Window2GUI("Window 2", 1024, 648, 235, 226, 204, False)	# Create instance of applications Window 2 (1024, 648)
window3 = Window3GUI("Window 3", 1024, 648, 204, 235, 223, False)	# Create instance of applications Window 3 (1024, 648)
window4 = Window4GUI("Window 4", 1024, 648, 204, 204, 235, False)	# Create instance of applications Window 4 (1024, 648)

stackedWidget = QStackedWidget()
stackedWidget.addWidget(window1)
stackedWidget.addWidget(window2)
stackedWidget.addWidget(window3)
stackedWidget.addWidget(window4)

stackedWidget.setWindowFlag(Qt.FramelessWindowHint)
stackedWidget.show()

#############################################################
# Create event loop
#############################################################

app.exec_()