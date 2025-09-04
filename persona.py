from datetime import date

class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calc_edad(cls, name, age):
        if date.today().month >= 6:
            return cls(name, (date.today().year -1) - age)
        return cls(name, date.today().year - age)
    
    def __str__(self):
        return f'Nombre: {self.name} Anno de nacimiento: {self.age}'
    
    @staticmethod
    def isAge(age):
        return age > 18

persona = Persona.calc_edad('Yoeny', 41)
print(persona.age)
if Persona.isAge(persona.age):
    print('Puede bailar')
else:
    print('no puede pasar')

def calcular(*args):
    return sum(args)/len(args)