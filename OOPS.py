# class Dog():
#     def __init__(self,breed, name, spots):
#         self.breed = breed
#         self.name = name
#         self.spots = spots
#
# my_dog = Dog(breed="Local", name="Oscar", spots=True)
#
# print(my_dog.name)



#
# class Dog():
#     ####Class object attribute
#     ####Same for any instance of a class
#     Species = "Mammal"
#
#     def __init__(self,breed, name, spots):      ####For user defined attribute
#         self.breed = breed
#         self.name = name
#         self.spots = spots
#
# my_dog = Dog(breed="Local", name="Oscar", spots=True)
#
# print(my_dog.Species)




#
class Dog():

    Species = "Mammal"

    def __init__(self,breed, name):
        self.breed = breed
        self.name = name

#     ####actions/operations----->METHODS i.e. a function which is inside a class
#     def bark(self):
#         print("Bhow Bhow!!! my name is: {}".format(self.name))
#
# my_dog = Dog("Local","Oscar")
# my_dog.bark()          #####we can call method of a class by putting () behind it brow



#     def bark(self,colour):
#         print("Bhow Bhow!!! my name is: {} and my colour is {}".format(self.name, colour)) ###look Bro...no self.colour
#                                                                                             ### here only colour
# my_dog = Dog("Local","Oscar")
# my_dog.bark(colour="black")          #####we can call method of a class by putting () behind it brow
#
#





#--------------------------------------------------------------------------------------------------


class Circle():

    pi = 3.1416     ####class object attribute

    #####METHOD
    def __init__(self,radius = 1):            ####radius default value is 1
        self.radius = radius
        self.area = radius * radius * self.pi

    def get_circumference(self):
        return (self.radius * self.pi * 2)

    # def area(self,area = 1):              ####another way
    #     return area * area * self.pi


my_circle = Circle(30)
print(type(my_circle))
print(Circle.pi)
print(my_circle.get_circumference())            ####notice not circle----> it's my_circle
print(my_circle.area)                           ####notice the () on area

