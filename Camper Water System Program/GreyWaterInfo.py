import piplates.DAQCplate as DAQC

class GreyWater:
	def getGreyWater():
		sensorInput = 0
		percUsed = 200
		while sensorInput == 0:
			try:
				sensorInput = DAQC.getADC(0, 1)
				if sensorInput > 0:
					percUsed = round(((3.8 - DAQC.getADC(0, 1))/(3.8-2.1))*100)
				time.sleep(2)
			except:
				print("")
		return percUsed
