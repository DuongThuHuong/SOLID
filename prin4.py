
class AnimalInterface:

    def Eat(self):
        raise NotImplementedError
    
    def Swim(self):
        raise NotImplementedError

    def Fly(self):
        raise NotImplementedError

    def Sleep(self):
        raise NotImplementedError

class Bird(AnimalInterface):
    
    def Eat(self):
        pass

    def Sleep(self):
        pass

    def Fly(self):
        pass

class Cat(AnimalInterface):

    def Eat(self):
        pass

    def Sleep(self):
        pass

    def Swim(self):
        pass

#### Interface Segregation Principle ####

class IAnimal:

    def Eat(self):
        raise NotImplementedError

    def Sleep(self):
        raise NotImplementedError

class IBird:

    def Fly(self):
        raise NotImplementedError

class ICat:

    def Swim(self):
        raise NotImplementedError

class Bird(IAnimal, IBird):

    def Eat(self):
        pass

    def Sleep(self):
        pass

    def Fly(self):
        pass

class Cat(IAnimal, IBird):

    def Eat(self):
        pass

    def Sleep(self):
        pass

    def Swim(self):
        pass
