import random
import string

class Dummy:

    marriaged = None
    parents = (None, None)

    def __init__(self):
        self.assets = []
        self.money = 100
        self.age = 0
        self.gender = getRandomGender()
        if self.parents[0] is not None:
            surname = self.parents[0]
        else:
            surname = getSurname()
        self.name =  getName(self.gender) +" "+ surname
        # Concepto de generacion

    def getMarriage(self, dummy):
        if dummy.age < 18:
            raise ValueError("Menor de edad!")
        elif dummy.age > 45:
            raise ValueError("Demasiado mayor")

        self.marriaged = dummy
        # The other one is marriaged with you
        dummy.marriaged = self

    def __repr__(self):
        return self.name


class DummyList:

    stack = []
    summary_data = []
    generation = 0
    year = 0

    def __init__(self, n):
        self.create_generation(n)

    def add(self, dummy):
        self.stack.append(dummy)

    def show_all(self):
        for dummy in self.stack:
            print """name: {name}
                        gender: {gender}
                        age: {age}
                        money: {money}
                        marriaged_with: {marriaged}""".format(name=dummy.name,
                                                             gender=dummy.gender,
                                                             age=dummy.age,
                                                             money=dummy.money,
                                                             marriaged=dummy.marriaged,
                                                             )

    def terminate(self, dummy):
        """ kills a dummy. Not a murder, Just a natural die"""
        if dummy in self.stack:
            self.stack.remove(dummy)

    def create_generation(self, n):
        """ create a generation of n individuos"""
        for i in range(n):
            self.stack.append(Dummy())
        self.generation += 1 
    
    def next_year(self):
        """ Displace time one year forward. It means all created dummies increase his age one year."""
        self.year +=1 
        for dummy in self.stack:
            dummy.age += 1
    
    def find_wife(self):
        """ Dummies can get marriage. This method try to find a partner to a male dummy. """
        for male in self._get_males():
            for female in self._get_females():
                try:
                    if 3 > random.randint(1,10):
                        male.getMarriage(female)
                except ValueError:
                    pass

    def get_couples(self):
        """ Return couples created by marriage. In this imaginary world only consider traditional marriages"""
        return [(dummy, dummy.marriaged) for dummy in self.stack if dummy.gender is 'male' and dummy.marriaged is not None]

    def set_babies(self):
        for couple in self.get_couples():
            if 2 > random.randint(1,10):
                baby = Dummy()
                baby.parents = couple
                self.add(baby)
            
    def symmary(self):
        pass

    def _get_females(self):
        return [dummy for dummy in self.stack if dummy.gender == 'female' and dummy.marriaged is None]
    
    def _get_males(self):
        return [dummy for dummy in self.stack if dummy.gender == 'male' and dummy.marriaged is None]    

def getSurname():

    lista_apellidos = ['Alvarez', 'Lopez', 'Martinez', 'Perez', 'Fernandez', 'Garcia', 'Sanchez', 'Rodriguez', 'Diaz', 'Sanz', 'Castellanos', 'Triguero', 'Gago', 'Ramos']     
    return lista_apellidos[random.randint(1, len(lista_apellidos)) -1]

def getName(gender):

    lista_nombres_masculinos = ['Daniel', 'Mario', 'Rodrigo', 'Jose', 'Ronaldo', 'Tom', 'Carlos', 'Julio', 'Alberto', 'Ricardo', 'Fernando', 'Roberto', 'Alfonso', 'Alonso']
    lista_nombres_femeninos = ['Monica', 'Rosa', 'Juana', 'Julia', 'Adela', 'Sara', 'Carmen', 'Ana', 'Imelda', 'Evelia']

    if gender is 'male':
        return lista_nombres_masculinos[random.randint(1, len(lista_nombres_masculinos)) -1]
    else: 
        return lista_nombres_femeninos[random.randint(1, len(lista_nombres_femeninos)) -1]

def getRandomGender():
    genders = ['male', 'female']
    return genders[random.randint(0,1)]

