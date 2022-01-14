import math
from scipy.integrate import quad
from fractions import Fraction

#archivo = open ("tablas.txt","w")

a = -6
b = 6



while True:

	n = 100000
	dx = (b - a)/(n)
	suma = 0
	
	for i in range (0,n+1):
		
		x = a + i*(dx)
		fx = (1/(math.sqrt(2*(math.pi))))*math.exp(-(x**2)/2)

		if i==0:
			integral = 1*fx
		elif 0<i<n:
			integral = 2*fx
		else:
			integral = 1*fx
		
		suma= suma + integral

	integralFinal = (dx/2)*(suma)
	print ("%.2f"% b ,"=", "%.10f" % integralFinal)
#	archivo.write( "%.2f  " % b) 
#	archivo.write( "%.10f\n" % integralFinal)
	
	b = b - 0.02
	
	if(b < a):
		break

#archivo.close()


