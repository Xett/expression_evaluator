import math
import random

def mod(a, b):
    return a % b

def pow(a, b):
    return a ** b

def append(a, b):
    if type(a) != list:
        return [a, b]
    a.append(b)
    return a

def concat(a, b,*args):
    result=u'{0}{1}'.format(a, b)
    for arg in args:
        result=u'{0}{1}'.format(result, arg)
    return result

def equal(a, b ):
    return a == b

def notEqual(a, b ):
    return a != b

def greaterThan(a, b ):
    return a > b

def lessThan(a, b ):
    return a < b

def greaterThanEqual(a, b ):
    return a >= b

def lessThanEqual(a, b ):
    return a <= b

def andOperator(a, b ):
    return ( a and b )

def orOperator(a, b ):
    return  ( a or  b )

def xorOperator(a, b ):
    return  ( a ^ b )

def inOperator(a, b):
    return a in b

def notOperator(a):
    return not a

def neg(a):
    return -a

def random(a):
    return random.random() * (a or 1)

def fac(a):  # a!
    return math.factorial(a)

def pyt(a, b):
    return math.sqrt(a * a + b * b)

def sind(a):
    return math.sin(math.radians(a))

def cosd(a):
    return math.cos(math.radians(a))

def tand(a):
    return math.tan(math.radians(a))

def asind(a):
    return math.degrees(math.asin(a))

def acosd(a):
    return math.degrees(math.acos(a))

def atand(a):
    return math.degrees(math.atan(a))

def roll(a, b):
    rolls = []
    roll = 0
    final = 0
    for c in range(1, a):
        roll = random.randint(1, b)
        rolls.append(roll)
    return rolls

def ifFunction(self,a,b,c):
    return b if a else c