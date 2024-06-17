#String exercise
age=26
txt="hii i am deva, my age is {}"
print(txt.format(age))

txt="only {price:.2f} thats it"
print(txt.format(price=49.98978))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt="i want {:*<5} chickens"
print(txt.format(49))

txt="i want {:^5} chickens"
print(txt.format(49))

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

txt="the value between {:+} and {:+}"
print(txt.format(-3,7))

txt="the value between {:} and {:}"
print(txt.format(-3,7))

txt="the value is {:,}"
print(txt.format(77650000))

txt="the value is{:_}"
print(txt.format(13000000000))


txt="we have more no of {:d}"
print(txt.format(0b101))

txt="the value is {:e}"      #scientific notation
print(txt.format(5))

txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

txt = " the vallue is {:.0%}"
print(txt.format(0.25))

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a="hii  \nhow"
print(a)

#String slicing exercise


txt="hello world"
print(txt[::-1])


for txt in "deva":
    print(txt)

txt="i am a barbie girl"
if "barbie" in txt:
    print("wow its correct")
else:
    print("oopsss.....")

txt="i am a barbie girl"
print( "deva" not in txt)

txt="hello, world"
print(txt[2:5])
print(txt[:5])            #slice from the strat
print(txt[3:])            #slice to the end
print(txt[-5:-2])         #negative indexing
print(txt[0:-5])
print(txt[::2])            #step     hor h,l
print(txt[::5])


#MODIFY STRINGS

txt="devadharshini wow"
print(txt.upper())
print(txt.lower())
print(txt.capitalize())
print(txt.title())
print(len(txt))
print(txt.strip())
print(txt.replace('d','m'))
print(txt.split())

#string concatenation

a="deva"
b=" cutie"
txt="above mentioned is {} is a {}"
print(txt.format(a,b))

txt= "happy birthday my dear\'s "
print(txt)
txt="happy birthday \"my\" angle"
print(txt)
txt="happmbirthday \rdevadharshini"
print(txt)
txt = "happy\r birthday!"
print(txt) 
txt="happy   \bbday"
print(txt)
txt="ha\tbday"
print(txt)

txt="what a beautyful woman"
print(txt.center(40,"*"))

# python operators

x=50
y=3
print(x//y)

#python lists
fruits=['apple','orange','mango','pineapple','banana']
print(fruits)
print(fruits[::2])
if "apple" in fruits:
    print('yes')
else:
    print('no')
fruits[0]='papaya'
print(fruits)
fruits.insert(1,'apple')
print(fruits)

fruits.append(222)
print(fruits)

fruits.remove('papaya')     #remove the element with specified value
print(fruits)

fruits.pop()
print(fruits)              #remove the element with specified index  clear is used to delete all the indexes

for x in fruits:
   print(x)

[print(x) for x in fruits]

newlist=[x for x in fruits if "a" in x]
print(newlist)

v=[x for x in range(10) if x<5]
print(v)
fruits.sort()
print(fruits)
print(sorted(fruits))

#scope
class name:
   def myfunc(fname):
     print("hello",fname)
   myfunc('deva')


   


