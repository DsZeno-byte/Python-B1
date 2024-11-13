from oops.dog import Dog
from oops.cat import Cat

from oops.Animal import Animal

dog1=Dog("D1",6)
cat2=Cat("c11",61)

print(dog1)
print(cat2)

print(isinstance(dog1,Dog))
print(isinstance(dog1,Cat))

print(isinstance(dog1,Animal))
print(isinstance(dog1,Animal))
