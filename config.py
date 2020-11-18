import random

def data():
	data1 = str(random.randint(10, 100)) + '°C'
	data2 = str(random.randint(10, 100)) + '°F'
	return data1, data2

updateTime = 3	#in second

layout = {
	'appTitle' : 'Application',
	'heading1Text' : 'TEMPRATURE in °C',
	'heading2Text' : 'TEMPRATURE in °F',
	'headingTextSize' : 50,
	'dataTextSize' : 100,
}