'''a = 33 
b = 80
if b > a:
 print("b is greater than a")


a = 33
b = 33
if b > a:
 print("b is greaer than a")
elif b == a:
 print("b and a is equal")

 
a = 300
b = 400
if a > b:
 print("a is greater than b")
elif a == b:
 ("print a and b is equal")
else:
 print("b is greater than a")


a = 9 
b = 10
if b < a:
 print("b is lesser than a")
else:
 print("b is greater than a")

a = 200
b = 100
if a > b: print("a is greater thana a")

a = 2
b = 1
print("a") if a < b else print("b")

a = 900
b = 900
print(a) if a > b else print("=")# if a == b else print(yes)''


a = 900
b = 800
c = 700
if a > b and c < a:
 print("both condition is true")

a = 200
b = 300
c == 400
if a > b or a < b :
 print("atleast one of the condition is true ")



a = 200
b = 100
if not b > a :
 print("not b is greater than a")

x = 60
if x  > 10:
 print("above ten,")
if x < 100:
  print("below 100,")
else:
  ("but not above 20")


x = 8
y = 7
if y > x :
 pass
#oython match
def week_day(day):
 match day :
  case 1:
    print("monday")
  case 2:
    print("tuesday")
  case 3:
    print("wednesday")
  case 4:
    print("thursday")
  case 5:
    print("friday")
  case 5:
   print("saturday")
  case 7:
    print("sunday")
week_day(3)

def week_day(day):
 match day :
  case 1:
   print("tuesday")
  case 2:
   print("friday")
  case _:
   print("lookong for forward to the weekend")
 

week_day(3)
  
day = 4
match day :
 case 1 | 2|3|4|5:
  print("today is weekend")
 case 7|9:
  print("today is not weekend")

 
month = 6 
day = 3
match day :
  case 1|2|3|4|5 if month == 5:
   print("weekend in april")
  case 1|2|4|5 if month == 6:
   print("weekend in march")
  case _:
    print("no match")

#python phython while loop

i = 1
while i < 5:
 print(i)
 i += 1
 
i = 1 
while i < 6:
 print(i)
 if (i == 3):
  break
 i += 1

i = 0
while i < 10:
  i += 1
  if i == 5:
   continue
  print(i)
  
i = 0
while i < 5:
  print(i) 
  i += 1
else:
 print("i is no longer than 6")


#python for loop


fruits = ["apple","banana","orange"]
for x in fruits:
 print(x)
 if x == "banana":
  break
 fruits = ["apple","banana","guava"]
for x in fruits:
 if x == "guava":
  break
 print(x)
   

fruits = {"apple","banana","cherry"}
for x in fruits:
 if x == "banaan":
  continue
 print(x)




for x in range(2,100,10):
 print(x)



for x in range (9):
 
 if x == 6:
  break  # - break show else other wise not 
 print(x)
else:
 print("finally finished")


fruits = ["apple","banana","orange"]
tropical = ["red","big","testy"]
for x in fruits:
 for y in tropical:
  print(x,y)



fruits = ["apple","banana","orange"]
tropical = ["red","big","testy"]
for x in range(len(fruits)):
 print(fruits[x]," = ",tropical[x])


for x in range(0,8,2):
 pass
 
#function 


def my_function():
 print("hello from my function")

my_function() 


def my_function(fname):
 print(fname + " batsman")

my_function("altamash")
my_function("danish")
my_function("ak")

def my_function(fname, lname):
 print(fname + lname)
my_function("altu"," danni")


def my_function(*kids):
 print( kids[2]+ ":" + kids[1] )  # child which you want also got like 236 line
my_function("shahista","azhar","altu")

def my_function(child1,child2,child3):
 print("elder child is " + child1)
my_function(child1="azhar",child2="altu",child3="shahista")


def my_function(**children):
 print("elder child is " + children["child2"])
my_function(child1="azhar",child2="altu",child3="shahista")

def my_function(country = "norway"):
 print("i am from " + country)
my_function()
my_function("india")
    


def my_function(food):
 for x in food :
   print(x)
fruits = ["apple","banana","litchi"]
my_function(fruits)

def my_function(food):
   print(fruits)
fruits = ["apple","banana","litchi"]
my_function(fruits)


def my_function(x):
 return 5 * x

print(my_function(5))


def my_function():
 pass

def my_function(x,/):
 print(x)
my_function(3)

def my_function(x) :
 print(x)
my_function(x = 8)  #(8) also work

def my_function(*,x):
 print(x)
my_function(x = 6)

def my_function(a,b, /,*,c,d):
 print(a+b+c+d)
my_function(9,8,c=6,d = 9)

def tri_recursion(k): 
 if (k > 0 ):
  result = k + tri_recursion(k-  1)
  print(result)
 else:
  result = 0
  
 return result
print("recursion example result") 
tri_recursion(6) 

#python lambda


x = lambda a: a+10
print(x(8))

x = lambda a,b : a * b
print(x(6,8))

x = lambda A,b,c :A+b+c
print(x(2,4,7))

def my_function(x):
 return lambda a : a * x
my_doubler = my_function(2)
print(my_doubler(11))

def my_function(x):
 return lambda a :a*x
my_tripler = my_function(3)
print(my_tripler(11))

def my_funtion(x):
 return lambda a : a * x
my_doubler = my_function(2)
my_tripler = my_function(3)
print(my_doubler(10))
print(my_tripler(10))

#array

car = ["toyto","ford","volvo"]
x = car[1]
print(x)

car = ["toyto","bmw","volvo"]
car[0] = "alto"
print(car)

car = ["toyto","alto","volvo"]
x = len(car)
print(x)

car = ["toyto","alto","bmw"]
for x in car:
 print(x)

car = ["ford","bmw","alto"]
car.append("maruti")
print(car)

car= ["ford","alto","bmw"]
car.pop(2)
print(car)

car = ["ford","alto","bmw"]
car.remove("alto")
print(car)

#python classes and object


class myclass():
 x = 5
print(myclass)


class myclass():
   x=6
p1 = myclass()
print(p1.x)


class myclass:
 def __init__(self,name,age):
  self.name =name
  self.age =age
p1 = myclass("altamash",23)
print(p1.name)
print(p1.age)



class person:
 def __init__(self,name,age):
   self.name = name
   self.age =  age


 def __str__(self):
    return f"{self.name}({self.age})"
p1 = person ("altu",23)
print(p1)


class person:
 def __init__(self,name,age):
  self.name = name
  self.age= age
 def my_function(self):
  print("he is ", self.name,"and their age is", self.age)
p1 = person("altu",23)
p1.my_function()




class persion:
 def __init__(altu,name,age):
  altu.name = name
  altu.age = age 
 def my_function(altu):
  print("my name is ", altu.name,"and he is ", altu.age)
p1 = person("danish",20)
p1.my_function()



class persion:
 def __init__(altu,name,age):
  altu.name = name
  altu.age = age 
 def my_function(altu):
  print("my name is ", altu.name,"and he is ", altu.age)
p1 = person("danish",20)
p1.age = 22
p1.name = "jabbu"
p1.my_function()  # print(p1.age can also use instead of this line)


class person :
 pass

#python inheritance

class person :
 def __init__(self,fname,lname):
  self.firstname = fname
  self.lastname = lname
 def printname(self):
  print(self.firstname, self.lastname)
x = person("altu","khan")
x.printname()

class person:
 def __init__(self,fname,lname)   :
  self.firstname = fname
  self.lastname =lname
 def printname(self):
  print(self.firstname, self.lastname)
class student(person):
  pass
x = student("altu" , "khan")
x.printname()



class person :
 def __init__(self,fname,lname):
  self.firstname = fname
  self.lastname = lname 
 def printname(self):
  print(self.firstname , self.lastname)
class student (person):
  def __init__(self,fname,lname):
   person.__init__(self,fname,lname)
  
  
x = student ("altu","khan")

x.printname()

class person :
 def __init__(self,fname,lname):
  self.firstname = fname 
  self.lastname  = lname
 def printname(self):
  print(self.firstname , self.lastname)
class student(person):
 def __init__(self,fname,lname):
  super().__init__(fname,lname)
x = student("danish", "khan")
x.printname()


class person :
 def __init__(self,fname,lname):
  self.fstname = fname 
  self.lstname = lname 
 def printname(self):
  print(self.fstname , self.lstname)

class student (person):
 def __init__(self,fname,lname):
  super().__init__(fname ,lname)
  self.graduationyear = 2019

x = student("jawed","khan")
print(x.graduationyear)




class person:
 def __init__(self,fname,lname):
  self.fstname = fname 
  self.lstname = lname
 def printname(self):
  print(self.fstname, self.lstname)

class student (person):
 def __init__(self,fname,lname,year):
  super().__init__(fname ,lname)
  self.graduationyear = year

x = student("jawed","khan", 2018)
print(x.graduationyear)


class person :
 def __init__(self,fname,lname,year):
  self.firstname = fname
  self.lastname = lname
  self.graduationyear = year
 def printname(self):
  print(self.firstname, self.lastname)
class student(person):
 def __init__(self,fname,lname,year):
  person.__init__(self,fname,lname,year)
 def welcome(self):
   print("welcome", self.firstname, self.lastname , "to the", self.graduationyear)   
   #self.graduationyear = year
x = student("shayan","khan",2025)
x.welcome()

   #python itetor 

mytuple = ("altamash","danish","jawed")   
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "altamash"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class mynumber:
 def __iter__(self):
  self.a = 1
  return self
 def __next__(self):
   x = self.a
   self.a += 1
   return x        # direct self . a can be used here if we erase upper 2nd line
x = iter(mynumber())  # myclass = mynumber()
                        #myiter = iter(myclass)
print(next(x))
print(next(x))


class mynumber :
 def __iter__(self):
  self.a = 1 
  return self 
 def __next__(self):
  if self.a <= 20 :
   x = self.a 
   self.a += 1
   return x
  else:
   raise StopIteration
y = iter(mynumber())
for x in y:
 print(x)


class mynumber :
 def __iter__(self):
  self.a = 1
  return self 
 def __next__(self):
  if self.a <= 20:
   x = self.a 
   self.a += 1
   return x
  else:
   raise StopIteration
myobj = mynumber()
myit = iter(myobj)
for x in myit:
 print(x)

#polymorphism

class car :
 def __init__(self,brand,model):
  self.brand = brand
  self.model = model 
 def move (self):
  print("drive")

class boat :
 def __init__(self,brand,model):
  self.brand =brand 
  self.model = model 
 def move (self):
  print("sail")

class aeroplane :
 def __init__(self,brand,model):
  self.brand = brand
  self.model = model
 def move (self):
  print("fly")
car1 = car("ford","mastang")
boat1= boat("incv","russia")
aeroplane1 = aeroplane("dubaiairline","f12")
for x in (car1,boat1,aeroplane1):
 print(x.brand)
 x.move()





class vechile :
 def __init__(self,model,brand):
  self.brand = brand 
  self.model = model 
 def move (self):
  print("move")

class car (vechile) :
 pass 

class boat(vechile):
 def move(self):
  print("sail")

class plane (vechile):
 def move (self):
  print("fly")

car1 = car("ford","mastang") 
boat1 = boat("ibizz","touring20")
plane1 = plane("boeing","747")
for x in (car1,boat1,plane1):
 print(x.brand)
 print(x.model)
 x.move()


#python scope

def myfunction():
 x = 200
 print(x)
myfunction()

def myfunction():
 x = 300
 def myinnerfunc():
   print(x)
 myinnerfunc()



x = 400
def myfunction():
 print(x)
myfunction()
print(x)


x = 600
def myfunction():
 y =700
 print(y)
myfunction()
print(x)

def myfunction():
  global x
  x = "altu"
myfunction()
print(x)

x = "danni"
def myfunction():
 global x 
 x = "jabbu"
myfunction()
print(x)


def myfunc1():
 x ="shayan"
 def myfunc2():
  nonlocal x
  x = "altamash"
 myfunc2()
 return x
print(myfunc1())


#python datetime

import datetime
x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

import datetime
x = datetime.datetime(1989,6,7,5,8,58)
print(x)
print(x.strftime("%Y"))


#python math 




x = max (10,20,30)
y = min (10,20,30)
print(x)

print(y)

x = abs(-7.9)
print(x)

x = pow(4,3)
print(x)

import math
x= math.sqrt(64)
print(x)
import math
x = math.ceil(19.2)
y = math.floor(19.2)
print(x,y)

x = math.pi
print(x)

import json
x = '{"name":"john","age":24,"city":"newyork"}'

y = json.loads(x)

print(y["city"])

x = {"name":"john",
     "age":19,
     "city":"delhi"}



y = json.dumps(x)
print(y)

print(type(y))
print(type(x))


print(json.dumps({"name":"jawed","age":19,"year":2025}))
print(json.dumps(["apple","banana","guava"]))
print(json.dumps(("car","buses","train")))
print(json.dumps(("apple")))
print(json.dumps((3,4,5)))
print(json.dumps((3.4,9.8,8.8)))
print(json.dumps((True)))
print(json.dumps((False)))
print(json.dumps((None)))

x = {"name":"jawed",
     "age":16,
     "country":"india",
     "married":True,
     "divorced":False,
     "children":("ann","billy"),
     "pets":None,
     "cars":[
      {"model":"bmw230","mpg":27.5},
      {"model":"ford edge","mpg":24.1}
  ]
}
y = json.dumps(x)
print(y)
print(type(y))

import json
x = {"name":"jawed",
     "age":16,
     "country":"india",
     "married":True,
     "divorced":False,
     "children":("ann","billy"),
     "pets":None,
     "cars":[
      {"model":"bmw230","mpg":27.5},
      {"model":"ford edge","mpg":24.1}
  ]
}
print(json.dumps(x, indent = 4))


x = {"name":"jawed",
     "age":16,
     "country":"india",
     "married":True,
     "divorced":False,
     "children":("ann","billy"),
     "pets":None,
     "cars":[
      {"model":"bmw230","mpg":27.5},
      {"model":"ford edge","mpg":24.1}
  ]
}

print(json.dumps(x,indent = 4, separators = (".",  " = " )))


x = {"name":"jawed",
     "age":16,
     "country":"india",
     "married":True,
     "divorced":False,
     "children":("ann","billy"),
     "pets":None,
     "cars":[
      {"model":"bmw230","mpg":27.5},
      {"model":"ford edge","mpg":24.1}
  ]
}

print(json.dumps(x, indent = 5, sort_keys=True ))
#regex
import re 

txt = "the rain in spain"
x = re.search("^the.*spain$", txt)
if x :
 print("yes we have a match")

else:
 print("no match")

txt = "the rain in spain"
x = re.findall("ai", txt)
print(x)

txt = "the rain in spain"
x = re.findall("portugal",txt)
print(x)
if x :
 print("yes there is atleast match ")
else:
 print("no match")


txt = "the rain in spain"
x = re.search("\s",txt)
print("the first white- space character located in position :",x.start())


txt = "the rain in spain"
x = re.search("portugal", txt)

print(x)

txt = "the rain in europe"

x = re.split("\s",txt)
print(x)

txt = "the rain in spain"
x = re.split("\s", txt,1)

print(x)



txt = "the rain in spain"
x = re.sub("\s","8", txt)

print(x)


txt = "the rain in spain"
x = re.sub("\s","7", txt, 1)

print(x)


txt = "the rain in spain"
x = re.search("ai",txt)
print(x)



txt = "the rain in spain"
x = re.search(r"\br\w+", txt)
print(x.span())


txt = "the rain in spain"

x = re.search(r"\br\w+", txt)
print(x.string)

txt = "the rain in spain"
x = re.search(r"\bt\w+", txt)

print(x.group())'''

#pip

'''import camelcase  #before use we should install camelcase
c = camelcase.CamelCase()
txt = "lorem ispum dollar sit amet"
print(c.hump(txt))'''


try:
 print(x)
except:
 print("an exception occured")

try:
 print(x)
except NameError:
 print("variable x is not defined")
except:
 print("something went wrong")

try:
 print("hello")

except:
 print("something went wrong")

else:
 print("nothing went wrong")

try:
 print("hello") #print(x) also work
except:
 print("something is went wrong")
                     
finally:
 print("the try except is finished")

try:
 f = open("demofile.txt") 
 try:
  f.write("lorum ipsum")
 except:
  print("something went wrong when writtig to the file")
 finally:
  f.close()
except:
 print("something went wrong when openning the file")


x = 2 #-1 found error
if x < 0:
 raise Exception("sory, no number below the zero")

x = "altu" # other than str found error
if not type(x) is str:
 raise TypeError ("only string are allowed")

#python string formatting 

txt = f"the price is 49 dollars"
print(txt)


price = 56
txt = f"the price is {price}, dollar"
print(txt)

price = 44
txt = f"the price is {price:.2f}, dollar"
print(txt)

txt = f"the price is {59:.2f}  dollar"
print(txt)

txt = f"the price is {20*6} dollar"

print(txt)

price = 59
tax = 0.24
txt = f"the price is {price + (price * tax)} dollar"
print(txt)

price = 28
txt = f"it is very {'expensive' if price > 40 else 'cheap'}"
print(txt)


fruits = "apple"
txt = f"i love {fruits.upper()}"
print(txt)


def myconverter(x):
 return x * 0.3048
txt = f"the plane is flying at a {myconverter(30000) }meter altitude"
print(txt)

price = 45000
txt = f"the price is {price:,} dollars"
print(txt)


quantity = 3
itemo = 567
price = 46
myorder = "i want {} piece of item number {} for {:.2f} dollars."
print(myorder.format(quantity,itemo,price))

age = 45
name = "john"
txt = "his name is {1}, {1}, is {0} years old"
print(txt.format(age,name))

myorder = "i have a {carname} and model is {model}"
print(myorder.format(carname = "ford" , model = "mastang"))


#python user input

'''print("enter your name")
name = input()

                      #print(f"hello{name}") can use

print("hello",format(name))

name =input("enter your name")

print(f"hello {name}")


name = input("enter your namr")
fav1= input("what is your favourite animal")
fav2 = input("what is your favorite color")
fav3 = input("what is your favorite number")
print(f"do you want a {fav1} {fav2} with {fav3} legs")'''



'''import math 
x = float(input("enter your number"))

y = math.sqrt(x)   # second option is math.sqrt(float/int(x))
print(f"the square root of {x} is {y}")'''

y = True  #supposed remove this line then loop never break cauz y is not defined or break is not using below
while y == True:   #while true: can use with last print indent and without indent all value are difference
 x = input("enter your number: ")
 try:
  x = float(x);
  y = False
 except:
  print("wrong input, please try again")
 
print("thank you")


#python virtual environment















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































