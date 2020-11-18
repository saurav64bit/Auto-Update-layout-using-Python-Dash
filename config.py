import random

def data():
	return str(random.randint(10, 100)) + '°C'

updateTime = 3	#in second

layout = {
	'appTitle' : 'Application',
	'headingText' : 'TEMPRATURE',
	'headingSize' : 50,
	'dataSize' : 100,
}