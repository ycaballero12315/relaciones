"""
Tarea video 1
"""

import random
 
 
class Personaje:
   """Clase para generar un personaje de RPG"""
 
   def _new_stat(self):
       dados = [random.randint(1, 6) for i in range(4)]
       dados.sort()
       max_dados = dados[1:]
       return sum(max_dados)
 
   def __init__(self, nombre):
       self.nombre = nombre
 
       self.fuerza = self._new_stat()
       self.destreza = self._new_stat()
       self.inteligencia = self._new_stat()
       self.sabiduria = self._new_stat()
       self.constitucion = self._new_stat()
 
   def show(self):
       return f"""{self.nombre}
   fuerza: {self.fuerza}
   destreza: {self.destreza}
   inteligencia: {self.inteligencia}
   sabiduria: {self.sabiduria}
   constitucion: {self.constitucion}
           """
 
 
p1 = Personaje("Eric")
 
print(p1.show())
