import math
from scipy.integrate import quad
from fractions import Fraction

print ( " -----------Distribucion Normal----------")
print ( " ------------------Menu------------------")
print ( " 1. El limite inferior tiende a menos infinito")
print ( " 2. El limite superior tiende a infinito")
print ( " 3. Ningun limite tiende a infinito")

opcion = float(input("Seleccione una opcion: "))

if opcion == 1:
	miu = float (input(" Ingrese Miu: "))
	sigma = float (input(" Ingrese Sigma: "))
	a = miu - (10*sigma)
	b = float (input(" Ingrese el limite superior: "))
	n = 100000
	dx = (b - a)/(n)
	suma = 0
	for i in range (0,n+1):
		
		x = a + i*(dx)
		fx = (1/(sigma*(math.sqrt(2*(math.pi)))))*math.exp(-(((x-miu)**2)/(2*(sigma**2))))

		if i==0:
			integral = 1*fx
		
		elif 0<i<n:
			integral = 2*fx

		else:
			integral = 1*fx

		suma= suma + integral

	integralFinal = (dx/2)*(suma)
	print( "La probabilidad del problema es:", "%.10f" % integralFinal)

elif opcion == 2:
	miu = float (input(" Ingrese Miu: "))
	sigma = float (input(" Ingrese Sigma: "))
	a = float (input(" Ingrese el limite inferior: "))
	b = miu + (10*sigma)
	n = 100000
	dx = (b - a)/(n)
	suma = 0
	for i in range (0,n+1):
	
		x = a + i*(dx)
		fx = (1/(sigma*(math.sqrt(2*(math.pi)))))*math.exp(-(((x-miu)**2)/(2*(sigma**2))))
	
		if i==0:
			integral = 1*fx
		
		elif 0<i<n:
			integral = 2*fx
	
		else:
			integral = 1*fx
	
		suma= suma + integral
	
	integralFinal = (dx/2)*(suma)
	print( "La probabilidad del problema es:", "%.10f" % integralFinal)


elif opcion == 3:

	miu = float (input(" Ingrese Miu: "))
	sigma = float (input(" Ingrese Sigma: "))
	a = float (input(" Ingrese el limite inferior: "))
	b = float (input(" Ingrese el limite superior: "))
	n = 100000
	dx = (b - a)/(n)
	suma = 0
	
	for i in range (0,n+1):
		
		x = a + i*(dx)
		fx = (1/(sigma*(math.sqrt(2*(math.pi)))))*math.exp(-(((x-miu)**2)/(2*(sigma**2))))
	
		if i==0:
			integral = 1*fx
		
		elif 0<i<n:
			integral = 2*fx
	
		else:
			integral = 1*fx	
 
		suma= suma + integral

	integralFinal = (dx/2)*(suma)
	print( "La probabilidad del problema es:", "%.10f" % integralFinal)

else:
	print ("Es una opcion invalida")






















 

