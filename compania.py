"""Video 2
Relaciones
"""

from personas import Empleado
from objetos import Tarjeta

t1 = Tarjeta("001")
e1 = Empleado("Eric", t1)

e1.fichar()
