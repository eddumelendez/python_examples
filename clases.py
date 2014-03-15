class Persona(object):

	def __init__(self, name, lastname):
		self.name = name
		self.lastname = lastname

	def saluda(self):
		print self.name

	def otroSaludo(self, mensaje):
		print mensaje, self.name

persona = Persona("Pepito", "Perez")
persona.saluda()
persona.otroSaludo("Hola")