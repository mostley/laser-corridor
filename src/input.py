import time
import RPi.GPIO as GPIO

class Input:
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)

		#Switch GPIO Pin
		self.switchGPIO = 7
		GPIO.setup(self.switchGPIO, GPIO.IN)

		#Button GPIO Pin
		self.buttonGPIO = 8
		GPIO.setup(self.buttonGPIO, GPIO.IN)
		
		#Quit Button GPIO Pin
		GPIO.setup(10, GPIO.IN)
		
		self.currentState = None
		self.previousState = None

	def isSwitchToggled(self):
		# Maybe read initial state in init method
		self.previousState = self.currentState
		self.currentState = GPIO.input(self.switchGPIO)
		#print('check state')
		if self.previousState == self.currentState:
			return None
		else:
			if self.currentState == GPIO.HIGH:
				return 'Start'
			else: 
				return 'Stopp'
	def readButton(self):
		buttonState = GPIO.input(self.buttonGPIO)
		if buttonState == GPIO.HIGH:
			return 'Pressed'

        def readQuitButton(self):
                buttonState = GPIO.input(10)
                if buttonState == GPIO.HIGH:
                        return 'Quit'

