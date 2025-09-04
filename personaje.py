"""
Tarea video 1
"""

import random
 
 
class Personaje:
    """Clase para generar un personaje de RPG"""
    def _new_start(self):
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.sort()
        max_dados = sum(dados[1:])
        return max_dados
    def __init__(self, nombre):
        self.nombre = nombre
        self.fuerza = self._new_start()
        self.valor = self._new_start()
        self.inteligencia = self._new_start()
        self.sabiduria = self._new_start()
        self.contitucion = self._new_start()
    
    def show(self):
        return(
            {'nombre': self.nombre, 
             'fuerza': self.fuerza, 'valor': self.valor,
             'inteligencia': self.inteligencia,
             'sabiduria': self.sabiduria,
             'constitucion': self.contitucion
             }
        )

p = Personaje('chanchito')
for k, v in p.show().items():
    print(f'{k}: {v}')
 
