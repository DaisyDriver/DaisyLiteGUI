from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, pyqtSignal, pyqtSlot
from PyQt5.QtCore import pyqtSignal

class SpeedButton(QPushButton):
	
	indexclick = pyqtSignal(int)
	
	def __init__(self, label, parent, index):
		super(SpeedButton, self).__init__(label, parent)
		
		self.index = index
		
		self.clicked.connect(self.onclick)
		
		self.setFixedSize(60, 60)
		
	def onclick(self):
		self.indexclick.emit(self.index)
		
	def anyclicked(self, index_in):
		if index_in == self.index:
			self.setChecked(True)
		else:
			self.setChecked(False)

class ManMoveSpeed(QGroupBox):
	
	def __init__(self, parent, daisydriver):
		super(ManMoveSpeed, self).__init__(parent)
		
		# announce parent
		self.parent = parent
		
		# announce daisydriver
		self.DD = daisydriver
		
		self.initUI()
		
		self.makeconnections()
		
		self.indexmanager(self.DD.speedval)
		
	def initUI(self):
		
		# general settings
		self.setTitle('Speed')
		
		layout = QVBoxLayout()
		
		self.but_high = SpeedButton('High', self, 2)
		self.but_high.setCheckable(True)
		self.but_med = SpeedButton('Medium', self, 1)
		self.but_med.setCheckable(True)
		self.but_low = SpeedButton('Low', self, 0)
		self.but_low.setCheckable(True)
		
		layout.addWidget(self.but_high)
		layout.addWidget(self.but_med)
		layout.addWidget(self.but_low)
		
		self.setLayout(layout)
		
		# set geometry
		self.setFixedSize(85, 245)
		
	@pyqtSlot(int)
	def indexmanager(self, index_in):
		self.but_high.anyclicked(index_in)
		self.but_med.anyclicked(index_in)
		self.but_low.anyclicked(index_in)
		
		self.DD.speedset(index_in)
		
	def makeconnections(self):
		self.but_high.indexclick.connect(self.indexmanager)
		self.but_med.indexclick.connect(self.indexmanager)
		self.but_low.indexclick.connect(self.indexmanager)
		
class XYbutton(QPushButton):
	
	def __init__(self, icon, parent, daisydriver, direction):
		super(XYbutton, self).__init__(icon, '', parent)
		
		# announce daisydriver
		self.DD = daisydriver
		
		# announce direction
		self.direction = direction
		
		# set geometry
		self.setFixedSize(60, 60)
		self.setIconSize(QSize(20, 20))
		
		# connect click
		self.pressed.connect(self.on_click)
		
	def on_click(self):
		# on click send jog info to daisydriver object
		self.DD.jog(self.direction, self)
		
class ManMoveXY(QGroupBox):
	
	def __init__(self, parent, daisydriver):
		super(ManMoveXY, self).__init__(parent)
		
		# announce parent
		self.parent = parent
		
		# announce daisydriver
		self.DD = daisydriver
		
		# initialise user interface
		self.initUI()
		
	def initUI(self):
		# general settings
		self.setTitle('X/Y plane')
		
		# XY controls, grid layout
		sublayout_XY = QGridLayout()
		
		# initialise widgets
		self.left = XYbutton(QIcon('resources/bubble_left.svg'), self.parent, self.DD, 'l')
		self.right = XYbutton(QIcon('resources/bubble_right.svg'), self.parent, self.DD, 'r')
		self.up = XYbutton(QIcon('resources/bubble_up.svg'), self.parent, self.DD, 'f')
		self.upright = XYbutton(QIcon('resources/bubble_upright.svg'), self.parent, self.DD, 'fr')
		self.upleft = XYbutton(QIcon('resources/bubble_upleft.svg'), self.parent, self.DD, 'fl')
		self.down = XYbutton(QIcon('resources/bubble_down.svg'), self.parent, self.DD, 'b')
		self.downright = XYbutton(QIcon('resources/bubble_downright.svg'), self.parent, self.DD, 'br')
		self.downleft = XYbutton(QIcon('resources/bubble_downleft.svg'), self.parent, self.DD, 'bl')
		
		# add widgets to vertical box layout
		sublayout_XY.addWidget(self.left, 1, 0, 1, 1)
		sublayout_XY.addWidget(self.right, 1, 2, 1, 1)
		sublayout_XY.addWidget(self.up, 0, 1, 1, 1)
		sublayout_XY.addWidget(self.upright, 0, 2, 1, 1)
		sublayout_XY.addWidget(self.upleft, 0, 0, 1, 1)
		sublayout_XY.addWidget(self.down, 2, 1, 1, 1)
		sublayout_XY.addWidget(self.downright, 2, 2, 1, 1)
		sublayout_XY.addWidget(self.downleft, 2, 0, 1, 1)
		
		# set sublayout as widget layout
		self.setLayout(sublayout_XY)
		
		# set geometry
		self.setFixedSize(220, 245)
		
class Zbutton(QPushButton):
	
	def __init__(self, icon, parent, daisydriver, direction):
		super(Zbutton, self).__init__(icon, '', parent)
		
		# announce daisydriver
		self.DD = daisydriver
		
		# announce direction
		self.direction = direction
		
		# set geometry
		self.setFixedSize(50, 87)
		self.setIconSize(QSize(28, 28))
		
		# connect click
		self.pressed.connect(self.on_click)
		
	def on_click(self):
		# on click send jog info to daisydriver object
		self.DD.jog(self.direction, self)

class ManMoveZ(QGroupBox):
	
	def __init__(self, parent, daisydriver):
		super(ManMoveZ, self).__init__(parent)
		
		# announce parent
		self.parent = parent
		
		# announce daisydriver
		self.DD = daisydriver
		
		# initialise user interface
		self.initUI()
		
	def initUI(self):
		# general settings
		self.setTitle('Z plane')
		
		# XY controls, grid layout
		sublayout_Z = QGridLayout()
		
		# initialise widgets
		self.up = Zbutton(QIcon('resources/arrowup.svg'), self.parent, self.DD, 'u')
		self.down = Zbutton(QIcon('resources/arrowdown.svg'), self.parent, self.DD, 'd')
		
		# add widgets to vertical box layout
		sublayout_Z.addWidget(self.up, 0, 0, 2, 1)
		sublayout_Z.addWidget(self.down, 2, 0, 2, 1)
		
		# set sublayout as widget layout
		self.setLayout(sublayout_Z)
		
		# set geometry
		self.setFixedSize(85, 245)

class ManualMovementSection(QGroupBox):
	
	def __init__(self, parent, camera, daisydriver):
		super(ManualMovementSection, self).__init__(parent)
		
		# announce parent (main window)
		self.main_window = parent
		
		# announce daisy driver handle
		self.DD = daisydriver
		
		# get customised PiCamera instance (need to know which camera/motors?)
		self.camera = camera
		
		# initialise user interface
		self.initUI()

	def initUI(self):
		# general settings
		self.setTitle('Manual Movement')
		
		# section layout
		sublayout_manmove = QHBoxLayout()
		
		# initialise widgets
		self.manSpeed = ManMoveSpeed(self, self.DD)
		self.manXY= ManMoveXY(self, self.DD)
		self.manZ = ManMoveZ(self, self.DD)

		# add widgets to vertical box layout
		sublayout_manmove.addWidget(self.manSpeed)
		sublayout_manmove.addWidget(self.manXY)
		sublayout_manmove.addWidget(self.manZ)

		# set sublayout as widget layout
		self.setLayout(sublayout_manmove)


