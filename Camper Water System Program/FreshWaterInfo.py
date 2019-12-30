import piplates.DAQCplate as DAQC

class FreshWater:
	def getFreshWater():
		sensorInput = 0
		percUsed = 200
		while sensorInput == 0:
			try:
				sensorInput = DAQC.getADC(0, 0)
				if sensorInput > 0:
					percUsed = round(((DAQC.getADC(0, 0) - 1.9)/(3.5-1.9))*100)
				time.sleep(2)
			except:
				print("")
		return percUsed