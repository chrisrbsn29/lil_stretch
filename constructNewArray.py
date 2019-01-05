from scipy import signal
import numpy as np

#stretchFactor is a percentage( 110% would be 1.10 ) and ogArray is a numpy 2D array
def constructNewArray(stretchFactor, ogArray):

	newNumRows = np.size(ogArray,0)
	newObjPerRow = stretchFactor * np.size(ogArray,1)
	newArray = np.zeros([newNumRows, newObjPerRow])

	for rowNum in range(np.size(ogArray,0)):
		newRow = signal.resample(ogArray[rowNum], newObjPerRow)
		newArray[rowNum] = newRow		
	return newArray
 
