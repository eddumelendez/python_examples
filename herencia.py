class Persona(object):

	def __init__(self, name, lastname):
		self.name = name
		self.lastname = lastname

	def saluda(self):
		print self.name

	def otroSaludo(self, mensaje):
		print mensaje, self.name

class Empleado(Persona):

	def __init__(self, name, lastname, jobTitle):
		self.name = name
		self.lastname = lastname
		self.jobTitle = jobTitle

	def saluda(self):
		print "hola", self.name

	def getJobTitle(self):
		return self.jobTitle

empleado = Empleado("Pepito", "Perez", "Manager")
empleado.saluda()
empleado.otroSaludo("Hola")
print empleado.getJobTitle()
