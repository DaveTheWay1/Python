# Overriding and Polymorphism
print("--Overriding--")
# * Overriding
# * to override, we simply use the same method name 
# * and change functionality  within the son:
class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!
# output:
# invoking PARENT method_a!
# invoking CHILD method_a!
print(" ")
print("--Polymorphism--")
# * Polymorphism
# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
    def pay_bill(self):
        print("Payment Not Specified.")
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")

a = Person()
milli = Millionaire()
student = GradStudent()
a.pay_bill()
milli.pay_bill()
student.pay_bill()

# * it seems that the main difference between overriding and polymorphism is that overriding 
# * simply takes the same method name and creates its own version of it while polymophism passes
# * the class through and then creates it's over version of it. Polymorphism ties them together.
# * just as the millionaire pays the person and the grad students ask the person if they can owe or 
# * wash the dishes for them.
# * being able to do multiple things witht he same function but based on scenario